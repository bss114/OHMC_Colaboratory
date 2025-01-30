from opentrons import protocol_api

requirements = {"robotType": "OT-2", "apiLevel": "2.21"}

# metadata
metadata = {
	'protocolName': 'Sample Transfer and Dilution in 96 Well Plates from CSV', 
	'author': 'J Bisanz, jordan.bisanz@gmail.com',
	'description': 'Cherry picks samples well by well of 96 well plate and transfer to a new plate with a specified concentration of diluent. A CSV of transfers must be provided at the time of transfer. See source for example.',
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
		description=("Table with 8 columns: SampleID, SourcePosition, SourceWell, DestPosition, DestWell, SampleConc, SampleVolume, DiluentVolume")
	)

def run(protocol: protocol_api.ProtocolContext):

	# parse the input
	loading_data = protocol.params.loadings.parse_as_csv()

	# load the plates for transfer
	source_slots = [row[1] for row in loading_data][1:]
	dest_slots = [row[3] for row in loading_data][1:]
	slots = source_slots + dest_slots
	unique_source_slots = list(set(slots))
	for slot in unique_source_slots: #example appears to have an extra :
		protocol.load_labware(
		load_name="biorad_96_wellplate_200ul_pcr",
		location=slot
	)

	# define labware, only load the plates that are specified in the csv file
	#SourcePlate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '1')
	#DestPlate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', '2')
	Diluent = protocol.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', '3') # eppendorf microcentrifuge tube in rack on position 3
	Tips = protocol.load_labware('opentrons_96_filtertiprack_20ul', '6') # 20ul filter tips on deck position 5

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
