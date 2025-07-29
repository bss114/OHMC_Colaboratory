from opentrons import protocol_api

requirements = {"robotType": "OT-2", "apiLevel": "2.21"}

# metadata
metadata = {
	'protocolName': 'Pool Equimolar libraries from CSV v0.12', 
	'author': 'J Bisanz, jordan.bisanz@gmail.com',
	'description': 'Cherry picking protocol to generate equimolar pools of sequencing libraries. All volumes are transferred to a single 1.5mL Eppendorf tube. Can load from 96 OR 384 well plates which is specified at runtime'
}

#Version history
#v0.1 - new script
#v0.11 - 7 July 2025 JB modified to reduce number of mixes in destination
#v0.12 - 23 July 2025 JB modified if load volume is zero, will skip well.

#Input csv format Example:
#SampleID	SourcePosition	SourceWell	Conc	Volume
#Patterson5_Mouse1_Veh1	1	A1	unknown	1
#Patterson5_Mouse1_Veh2	1	B1	unknown	1
#Patterson5_Mouse1_Veh3	1	C1	unknown	1
#Patterson5_Mouse1_Veh4	1	D1	unknown	1
#Patterson5_Mouse1_Veh5	1	E1	unknown	1
#Patterson5_Mouse1_Veh6	1	F1	unknown	1
#Patterson5_Mouse1_PFOS1	1	G1	unknown	1

def add_parameters(parameters):
	parameters.add_csv_file(
		variable_name="loadings",
		display_name="Loading volumes for diluton",
		description=("Table with 5 columns: SampleID, SourcePosition, SourceWell, Conc, Volume")
	)
	parameters.add_int(
		variable_name="newtube_volume",
		display_name="New tube volume",
		default=1200,
		minimum=50,
		maximum=2000,
		description=("At what volume (in ul) should the collection tube be replaced?")
	)
	parameters.add_bool(
		variable_name="ChangeTip",
		display_name="Change tips",
		default=True,
		description=("Should tips be changed between samples?")
	)
	parameters.add_int(
		variable_name="ChangeFrequency",
		display_name="Tip change frequency",
		default=8,
		minimum=1,
		maximum=96,
		description=("How frequently should tips be changed if ChangeTip=true? 1=every sample, 8=every column")
	)
	parameters.add_str(
		variable_name="PlateType",
		display_name="Plate Type",
		default="biorad_384_wellplate_50ul",
		choices=[
			{"display_name": "VWR/Biorad 96", "value": "biorad_96_wellplate_200ul_pcr"},
			{"display_name": "Biorad 384", "value": "biorad_384_wellplate_50ul"}
		],
		description=("Are samples in 96 or 384 well plates?")
	)	
	parameters.add_int(
		variable_name="PoolLocation",
		display_name="Pool Location",
		default=3,
		minimum=3,
		maximum=10,
		description=("Where is the eppi tube collecting libraries on the deck? Assuming in A1 of tube rack.")
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
	
	loadings_parsed = protocol.params.loadings.parse_as_csv()

	# load the plates for transfer
	source_slots = [row[1] for row in loadings_parsed][1:]
	unique_source_slots = list(set(source_slots))
	for slot in unique_source_slots:
		protocol.load_labware(
		load_name=protocol.params.PlateType,
		location=slot
		)

	epitube = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', protocol.params.PoolLocation) # eppendorf microcentrifuge tube in rack on position 3
	tips = protocol.load_labware('opentrons_96_filtertiprack_20ul', protocol.params.TipLocation) # 20ul filter tips on deck position 10

	# define pipettes
	p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[tips])

	i=0 # a counter to know when to change tips
	total_volume = 0 # tracking the total volume in the tube
	p20.pick_up_tip()
	for index, row in enumerate(loadings_parsed[1::]):
		source_position=row[1]
		source_well=row[2]
		sample_volume=float(row[4])
		source_location = protocol.deck[source_position][source_well]
		
		check = i % float(protocol.params.ChangeFrequency) #checking the remainder to know when to change tips
		if protocol.params.ChangeTip and check == 0 and i != 0:
			p20.drop_tip()
			p20.pick_up_tip()

		if sample_volume>0:
			p20.aspirate(sample_volume, source_location)
			p20.dispense(sample_volume, epitube['A1'])
			p20.mix(1,5)
			p20.blow_out()
		
		i=i+1
		total_volume = total_volume + sample_volume
		if total_volume > float(protocol.params.newtube_volume):
			protocol.home()	
			protocol.comment("Total volume is currently" + str(total_volume) + " ul")
			protocol.pause("Please insert new 1.5mL eppendorf tube")
			total_volume = 0
	p20.drop_tip()
