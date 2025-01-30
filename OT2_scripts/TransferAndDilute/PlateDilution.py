from opentrons import protocol_api

requirements = {"robotType": "OT-2", "apiLevel": "2.21"}

# metadata
metadata = {
	'protocolName': 'Transfer and Dilute Samples', 
	'author': 'J Bisanz, jordan.bisanz@gmail.com',
	'description': 'Transfers/rearrays samples to/from 96 or 384 well plates. Controlled with input csv. See source for layout.',
}

#Input csv format Example:
#SSampleID,SourcePosition,SourceWell,DestPosition,DestWell,SampleConc,SampleVolume,DiluentVolume
#Source Position is the source deck position, DesPosition is the destination deck position. The SampleConc column is not actually used but left in for simplicity when calculating in excel.
#Note the below examples is tsv from excel, need to save as csv
#SampleID	SourcePosition	SourceWell	DestPosition	DestWell	SampleConc	SampleVolume	DiluentVolume
#Patterson5_Mouse1_Veh1	1	A1	2	A1	11.764	3.40	2.60
#Patterson5_Mouse1_Veh2	1	B1	2	B1	19.015	2.10	3.90
#Patterson5_Mouse1_Veh3	1	C1	2	C1	19.968	2.00	4.00
#Patterson5_Mouse1_Veh4	1	D1	2	D1	25.499	1.57	4.43
#Patterson5_Mouse1_Veh5	1	E1	2	E1	11.419	3.50	2.50


def add_parameters(parameters):
	parameters.add_csv_file(
		variable_name="loadings",
		display_name="Loading volumes for diluton",
		description=("Table with 8 columns, see source or example in this folder")
	)
	parameters.add_str(
		variable_name="SourcePlateType",
		display_name="Source Plate Type",
		default="biorad_96_wellplate_200ul_pcr",
		choices=[
			{"display_name": "VWR/Biorad 96", "value": "biorad_96_wellplate_200ul_pcr"},
			{"display_name": "Biorad 384", "value": "biorad_384_wellplate_50ul"}
		],
		description=("Are samples in 96 or 384 well plates?")
	)
	parameters.add_str(
		variable_name="DestPlateType",
		display_name="Destination Plate Type",
		default="biorad_96_wellplate_200ul_pcr",
		choices=[
			{"display_name": "VWR/Biorad 96", "value": "biorad_96_wellplate_200ul_pcr"},
			{"display_name": "Biorad 384", "value": "biorad_384_wellplate_50ul"}
		],
		description=("Are samples in 96 or 384 well plates?")
	)	
	parameters.add_int(
		variable_name="DiluentLocation",
		display_name="Diluent Location",
		default=3,
		minimum=3,
		maximum=10,
		description=("Where is the eppi tube of diluent located? Assuming in A1 of tube rack.")
	)
	parameters.add_int(
		variable_name="TipLocation",
		display_name="Tip Location",
		default=4,
		minimum=3,
		maximum=10,
		description=("Where are the tips located? Assuming a max of 96 samples to be transf.")
	)

	

def run(protocol: protocol_api.ProtocolContext):

	# parse the input
	loading_data = protocol.params.loadings.parse_as_csv()

	# load the plates for transfer
	source_slots = [row[1] for row in loading_data][1:]
	unique_source_slots = list(set(source_slots))
	for slot in unique_source_slots:
		protocol.load_labware(
		load_name=protocol.params.SourcePlateType,
		location=slot
	)

	dest_slots = [row[3] for row in loading_data][1:]
	unique_source_slots = list(set(dest_slots))
	for slot in unique_source_slots:
		protocol.load_labware(
		load_name=protocol.params.DestPlateType,
		location=slot
	)


	# define labware, only load the plates that are specified in the csv file
	#SourcePlate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '1')
	#DestPlate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '2')
	Diluent = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', protocol.params.DiluentLocation) # eppendorf microcentrifuge tube in rack on position 3
	Tips = protocol.load_labware('opentrons_96_filtertiprack_20ul', protocol.params.TipLocation) # 20ul filter tips on deck position 5

	# define pipettes
	p20 = protocol.load_instrument('p20_single_gen2', 'left', tip_racks=[Tips])


	#loop through every line in the csv to be transferred to get the diluent
	p20.pick_up_tip()
	for index, row in enumerate(loading_data[1::]):
		source_position=row[1]
		source_well=row[2]
		dest_position=row[3]
		dest_well=row[4]
		sample_volume=float(row[6])
		diluent_volume=float(row[7])
		source_location = protocol.deck[source_position][source_well]
		dest_location = protocol.deck[dest_position][dest_well]
	
		if diluent_volume>0:
			p20.aspirate(diluent_volume, Diluent['A1'])
			p20.dispense(diluent_volume,dest_location)
	p20.drop_tip()

	#loop through every line in the csv to be transferred to get the sample
	for index, row in enumerate(loading_data[1::]):
		source_position=row[1]
		source_well=row[2]
		dest_position=row[3]
		dest_well=row[4]
		sample_volume=float(row[6])
		diluent_volume=float(row[7])
		source_location = protocol.deck[source_position][source_well]
		dest_location = protocol.deck[dest_position][dest_well]
	
		p20.transfer(
			volume=sample_volume,
			source=source_location,
			dest=dest_location
		)
