from opentrons import protocol_api

requirements = {"robotType": "OT-2", "apiLevel": "2.21"}

# metadata
metadata = {
	'protocolName': 'Conduct Bead Cleanup from 96-well Plates', 
	'author': 'J Bisanz, jordan.bisanz@gmail.com',
	'description': 'Do magnetic capture cleanup (Ampure or Homemade) from 96 well plates. Elutes to a new 96 well plate and operates column by column.'
}



def add_parameters(parameters):
	parameters.add_int(
		variable_name="StartingColumn",
		display_name="Starting Column",
		default=1,
		minimum=1,
		maximum=12,
		description=("Which column should bead cleanup start on?")
	)
	parameters.add_int(
		variable_name="EndingColumn",
		display_name="Ending Column",
		default=12,
		minimum=1,
		maximum=12,
		description=("Which column should bead cleanup end on?")
	)
	parameters.add_int(
		variable_name="ReactionVolume",
		display_name="Reaction Volume",
		default=20,
		minimum=10,
		maximum=50,
		description=("What volume (in ul) are our PCR reactions?")
	)
	parameters.add_float(
		variable_name="BeadRatio",
		display_name="Bead Ratio",
		default=1.8,
		minimum=0.6,
		maximum=1.8,
		description=("What is the bead ratio for cleanup? Bead volume will be 1.8 x reaction volume.")
	)
	parameters.add_int(
		variable_name="EtOHVolume",
		display_name="Wash Volume",
		default=125,
		minimum=50,
		maximum=150,
		description=("Ethanol wash volume (80% EtOH).")
	)
	parameters.add_int(
		variable_name="ElutionVolume",
		display_name="Elution Volume",
		default=20,
		minimum=15,
		maximum=50,
		description=("Required volume will be 5ul less than requested volume.")
	)
	parameters.add_float(
		variable_name="AspirationSpeed",
		display_name="Aspiration Speed",
		default=0.05,
		minimum=0.005,
		maximum=1,
		description=("How fast should liquids be aspirated off beads this a relative measurement from 94.ul/sec.")
	)
	parameters.add_float(
		variable_name="CaptureDepth",
		display_name="Capture Depth",
		default=1,
		minimum=0,
		maximum=5,
		description=("How far from bottom of well should the tip be in mm?")
	)

#Don't edit below this line unless you want to change the functionality of the script

def run(protocol: protocol_api.ProtocolContext):
	
	Magmodule = protocol.load_module('magnetic module gen2', 1)
	PCRplate = Magmodule.load_labware('biorad_96_wellplate_200ul_pcr')
	Elutionplate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', 2)
	EtOH=protocol.load_labware('agilent_1_reservoir_290ml', 4) # 400ul per reaction
	BeadsAndWater=protocol.load_labware('nest_12_reservoir_15ml', 5) # Beads in A1, Water in A2
	Waste = protocol.load_labware('agilent_1_reservoir_290ml', 3)
	
	# set up tips
	Ntips = ((protocol.params.EndingColumn - protocol.params.StartingColumn) + 1) * 8 * 4 / 96
	Ntips = int(Ntips) + (1 if Ntips > int(Ntips) else 0) # round up to nearest box
	
	protocol.comment("Using " + str(Ntips) + " boxes of tips")
	Tips = [protocol.load_labware('opentrons_96_filtertiprack_200ul', slot) for slot in range(1+6, Ntips+7)] # start loading at position 7 (6 + 1)
	mp200 = protocol.load_instrument('p300_multi_gen2', 'right', tip_racks=Tips)
	
	
	# add beads to all 
	protocol.comment("Adding " + str(protocol.params.BeadRatio * protocol.params.ReactionVolume) + " beads to columns " + str(protocol.params.StartingColumn) + " to " + str(protocol.params.EndingColumn))
	for col in range(protocol.params.StartingColumn, protocol.params.EndingColumn+1):
		if col == 1:
			mp200.pick_up_tip(Tips[0]['A1'])
			mp200.mix(repetitions=10, volume=150, location=BeadsAndWater['A1'])
		else: 
			mp200.pick_up_tip(Tips[0]['A'+str(col)])
		mp200.aspirate(protocol.params.BeadRatio * protocol.params.ReactionVolume, BeadsAndWater['A1'])
		mp200.dispense(protocol.params.BeadRatio * protocol.params.ReactionVolume, PCRplate['A'+str(col)])
		mp200.mix(repetitions=10, volume=(protocol.params.BeadRatio * protocol.params.ReactionVolume * 0.5), location=PCRplate['A'+str(col)])
		mp200.return_tip()
		
	Magmodule.engage()
	protocol.delay(minutes=1) # wait 1 minute for capture

	# now loop through column by column processing
	for col in range(protocol.params.StartingColumn, protocol.params.EndingColumn+1):
		protocol.comment("Cleaning up " + str(col))
		mp200.pick_up_tip(Tips[0]['A'+str(col)])
		mp200.aspirate(protocol.params.BeadRatio * protocol.params.ReactionVolume-2, PCRplate['A'+str(col)].bottom(protocol.params.CaptureDepth), rate=protocol.params.AspirationSpeed)
		mp200.air_gap(volume=10)
		mp200.dispense(protocol.params.BeadRatio * protocol.params.ReactionVolume+8, Waste['A1'].bottom(20)) # 20 mm off bottom to avoid dirtying tip
		mp200.drop_tip()
		
		#do two ethanol washes
		for i in range(0,2):
			mp200.pick_up_tip()
			mp200.aspirate(protocol.params.EtOHVolume, EtOH['A1'])
			mp200.air_gap(volume=10)
			mp200.dispense(protocol.params.EtOHVolume+10, PCRplate['A'+str(col)])
			protocol.delay(minutes=0.1)
			mp200.aspirate(protocol.params.EtOHVolume, PCRplate['A'+str(col)].bottom(protocol.params.CaptureDepth), rate=protocol.params.AspirationSpeed)
			mp200.air_gap(volume=10)
			mp200.dispense(protocol.params.EtOHVolume+10, Waste['A1'].bottom(20)) # 20 mm off bottom to avoid dirtying tip
			# on second wash do extra cleanup
			if i == 1:
				mp200.aspirate(protocol.params.EtOHVolume, PCRplate['A'+str(col)].bottom(protocol.params.CaptureDepth), rate=protocol.params.AspirationSpeed)
				mp200.dispense(protocol.params.EtOHVolume, Waste['A1'].bottom(20)) # 20 mm off bottom to avoid dirtying tip
			mp200.drop_tip()
		
		#add water
		mp200.pick_up_tip()
		mp200.aspirate(protocol.params.ElutionVolume, BeadsAndWater['A2'])
		Magmodule.disengage()
		mp200.dispense(protocol.params.ElutionVolume, PCRplate['A'+str(col)])
		mp200.mix(repetitions=10, volume=(protocol.params.ElutionVolume * 0.5), location=PCRplate['A'+str(col)])
		mp200.blow_out()
		Magmodule.engage()
		protocol.delay(minutes=0.5)
		mp200.aspirate(protocol.params.ElutionVolume-5, PCRplate['A'+str(col)].bottom(protocol.params.CaptureDepth), rate=protocol.params.AspirationSpeed)
		mp200.dispense(protocol.params.ElutionVolume-5, Elutionplate['A'+str(col)])
		mp200.drop_tip()
	
	