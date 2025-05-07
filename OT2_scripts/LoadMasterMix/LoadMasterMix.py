from opentrons import protocol_api

requirements = {"robotType": "OT-2", "apiLevel": "2.21"}

# metadata
metadata = {
	'protocolName': 'Load Mastermix into 384 well plate v0.1', 
	'author': 'J Bisanz, jordan.bisanz@gmail.com',
	'description': 'Loads master mix from 12-well reservoir to 384 well plates. This can be done in 1 or 2 plate simultaneously including for amplicon lib prep.'
}


def add_parameters(parameters):
	parameters.add_int(
		variable_name="volume",
		display_name="Master Mix Volume",
		default=9,
		minimum=1,
		maximum=20,
		description=("What volum should be loaded")
	)
	parameters.add_str(
		variable_name="MMwell",
		display_name="Reservoir Well",
		default="A1",
		choices=[
			{"display_name": "A1", "value": "A1"},
			{"display_name": "A2", "value": "A2"},
			{"display_name": "A3", "value": "A3"},
			{"display_name": "A4", "value": "A4"},
			{"display_name": "A5", "value": "A5"},
			{"display_name": "A6", "value": "A6"},
			{"display_name": "A7", "value": "A7"},
			{"display_name": "A8", "value": "A8"},
			{"display_name": "A9", "value": "A9"},
			{"display_name": "A10", "value": "A10"},
			{"display_name": "A11", "value": "A11"},
			{"display_name": "A12", "value": "A12"}
		],
		description=("Which well of the reservoir contains the mastermix?")
	)	
	parameters.add_bool(
		variable_name="LoadPlate1",
		display_name="Should Plate 1 be loaded?",
		default=True,
		description=("All wells of the 384 well plate 1 will be loaded")
	)
	parameters.add_bool(
		variable_name="LoadPlate2",
		display_name="Should Plate 2 be loaded?",
		default=True,
		description=("If true, Plate 2 will be loaded but only half the plate in the A1 and B1 corner wells")
	)
	parameters.add_int(
		variable_name="ResLocation",
		display_name="Reservoir Location",
		default=4,
		minimum=3,
		maximum=10,
		description=("Where is the reservoir located?")
	)
	parameters.add_int(
		variable_name="TipLocation",
		display_name="Tip Location",
		default=7,
		minimum=3,
		maximum=10,
		description=("Where are the tips located? Assuming a max of 96 samples to be transf.")
	)



#Don't edit below this line unless you want to change the functionality of the script

def run(protocol: protocol_api.ProtocolContext):
	


	
	reservoir = protocol.load_labware('nest_12_reservoir_15ml', protocol.params.ResLocation)
	mastermix = protocol.deck[protocol.params.ResLocation][protocol.params.MMwell]
	tips = protocol.load_labware('opentrons_96_filtertiprack_20ul', protocol.params.TipLocation)

	mm_volume=float(protocol.params.volume)
	
	# define pipettes
	mp20 = protocol.load_instrument('p20_multi_gen2', 'right', tip_racks=[tips])

	if protocol.params.LoadPlate1:
		plate1 = protocol.load_labware('biorad_384_wellplate_50ul', '1')
		dest_wells = [plate1.wells()[i] for i in range(0, 384, 16)] # every 16th number is a new column		
		mp20.transfer(volume=mm_volume, source=mastermix, dest=dest_wells)
		dest_wells = [plate1.wells()[i] for i in range(1, 384, 16)] 
		mp20.transfer(volume=mm_volume, source=mastermix, dest=dest_wells)
	
	if protocol.params.LoadPlate2:
		plate2=protocol.load_labware('biorad_384_wellplate_50ul', '2')
		dest_wells = [plate2.wells()[i] for i in range(0, 384, 32)] # every 32 number is everyother column		
		mp20.transfer(volume=mm_volume, source=mastermix, dest=dest_wells)
		dest_wells = [plate2.wells()[i] for i in range(1, 384, 32)] 	
		mp20.transfer(volume=mm_volume, source=mastermix, dest=dest_wells)
