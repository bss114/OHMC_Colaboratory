from opentrons import protocol_api

requirements = {"robotType": "OT-2", "apiLevel": "2.21"}

# metadata
metadata = {
	'protocolName': 'Set up 384-well qPCR from 96 well plate v0.1', 
	'author': 'J Bisanz, jordan.bisanz@gmail.com',
	'description': 'Loads master mix from 12-well reservoir to 384 well plates, and then add template from 96 well plate.'
}

#SideBySide layout
#Row	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24
#A	A1	A1	A1	A2	A2	A2	A3	A3	A3	A4	A4	A4	A5	A5	A5	A6	A6	A6	A7	A7	A7	A8	A8	A8
#B	A9	A9	A9	A10	A10	A10	A11	A11	A11	A12	A12	A12										STD	STD	STD
#C	B1	B1	B1	B2	B2	B2	B3	B3	B3	B4	B4	B4	B5	B5	B5	B6	B6	B6	B7	B7	B7	B8	B8	B8
#D	B9	B9	B9	B10	B10	B10	B11	B11	B11	B12	B12	B12										STD	STD	STD
#E	C1	C1	C1	C2	C2	C2	C3	C3	C3	C4	C4	C4	C5	C5	C5	C6	C6	C6	C7	C7	C7	C8	C8	C8
#F	C9	C9	C9	C10	C10	C10	C11	C11	C11	C12	C12	C12										STD	STD	STD
#G	D1	D1	D1	D2	D2	D2	D3	D3	D3	D4	D4	D4	D5	D5	D5	D6	D6	D6	D7	D7	D7	D8	D8	D8
#H	D9	D9	D9	D10	D10	D10	D11	D11	D11	D12	D12	D12										STD	STD	STD
#I	E1	E1	E1	E2	E2	E2	E3	E3	E3	E4	E4	E4	E5	E5	E5	E6	E6	E6	E7	E7	E7	E8	E8	E8
#J	E9	E9	E9	E10	E10	E10	E11	E11	E11	E12	E12	E12										STD	STD	STD
#K	F1	F1	F1	F2	F2	F2	F3	F3	F3	F4	F4	F4	F5	F5	F5	F6	F6	F6	F7	F7	F7	F8	F8	F8
#L	F9	F9	F9	F10	F10	F10	F11	F11	F11	F12	F12	F12										STD	STD	STD
#M	G1	G1	G1	G2	G2	G2	G3	G3	G3	G4	G4	G4	G5	G5	G5	G6	G6	G6	G7	G7	G7	G8	G8	G8
#N	G9	G9	G9	G10	G10	G10	G11	G11	G11	G12	G12	G12										STD	STD	STD
#O	H1	H1	H1	H2	H2	H2	H3	H3	H3	H4	H4	H4	H5	H5	H5	H6	H6	H6	H7	H7	H7	H8	H8	H8
#P	H9	H9	H9	H10	H10	H10	H11	H11	H11	H12	H12	H12										STD	STD	STD

#Integra layout
#Row	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24
#A	A1	A1	A2	A2	A3	A3	A4	A4	A5	A5	A6	A6	A7	A7	A8	A8	A9	A9	A10	A10	A11	A11	A12	A12
#B	A1		A2		A3		A4		A5		A6		A7		A8		A9		A10	STD1	A11	STD1	A12	STD1
#C	B1	B1	B2	B2	B3	B3	B4	B4	B5	B5	B6	B6	B7	B7	B8	B8	B9	B9	B10	B10	B11	B11	B12	B12
#D	B1		B2		B3		B4		B5		B6		B7		B8		B9		B10	STD2	B11	STD2	B12	STD2
#E	C1	C1	C2	C2	C3	C3	C4	C4	C5	C5	C6	C6	C7	C7	C8	C8	C9	C9	C10	C10	C11	C11	C12	C12
#F	C1		C2		C3		C4		C5		C6		C7		C8		C9		C10	STD3	C11	STD3	C12	STD3
#G	D1	D1	D2	D2	D3	D3	D4	D4	D5	D5	D6	D6	D7	D7	D8	D8	D9	D9	D10	D10	D11	D11	D12	D12
#H	D1		D2		D3		D4		D5		D6		D7		D8		D9		D10	STD4	D11	STD4	D12	STD4
#I	E1	E1	E2	E2	E3	E3	E4	E4	E5	E5	E6	E6	E7	E7	E8	E8	E9	E9	E10	E10	E11	E11	E12	E12
#J	E1		E2		E3		E4		E5		E6		E7		E8		E9		E10	STD5	E11	STD5	E12	STD5
#K	F1	F1	F2	F2	F3	F3	F4	F4	F5	F5	F6	F6	F7	F7	F8	F8	F9	F9	F10	F10	F11	F11	F12	F12
#L	F1		F2		F3		F4		F5		F6		F7		F8		F9		F10	STD6	F11	STD6	F12	STD6
#M	G1	G1	G2	G2	G3	G3	G4	G4	G5	G5	G6	G6	G7	G7	G8	G8	G9	G9	G10	G10	G11	G11	G12	G12
#N	G1		G2		G3		G4		G5		G6		G7		G8		G9		G10	STD7	G11	STD7	G12	STD7
#O	H1	H1	H2	H2	H3	H3	H4	H4	H5	H5	H6	H6	H7	H7	H8	H8	H9	H9	H10	H10	H11	H11	H12	H12
#P	H1		H2		H3		H4		H5		H6		H7		H8		H9		H10	NTC	H11	NTC	H12	NTC

#Legacy
#Row	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24
#A	A1	A2	A3	A4	A5	A6	A7	A8	A9	A10	A11	A12	A1	A2	A3	A4	A5	A6	A7	A8	A9	A10	A11	A12
#B	A1	A2	A3	A4	A5	A6	A7	A8	A9	A10	A11	A12										STD	STD	STD
#C	B1	B2	B3	B4	B5	B6	B7	B8	B9	B10	B11	B12	B1	B2	B3	B4	B5	B6	B7	B8	B9	B10	B11	B12
#D	B1	B2	B3	B4	B5	B6	B7	B8	B9	B10	B11	B12										STD	STD	STD
#E	C1	C2	C3	C4	C5	C6	C7	C8	C9	C10	C11	C12	C1	C2	C3	C4	C5	C6	C7	C8	C9	C10	C11	C12
#F	C1	C2	C3	C4	C5	C6	C7	C8	C9	C10	C11	C12										STD	STD	STD
#G	D1	D2	D3	D4	D5	D6	D7	D8	D9	D10	D11	D12	D1	D2	D3	D4	D5	D6	D7	D8	D9	D10	D11	D12
#H	D1	D2	D3	D4	D5	D6	D7	D8	D9	D10	D11	D12										STD	STD	STD
#I	E1	E2	E3	E4	E5	E6	E7	E8	E9	E10	E11	E12	E1	E2	E3	E4	E5	E6	E7	E8	E9	E10	E11	E12
#J	E1	E2	E3	E4	E5	E6	E7	E8	E9	E10	E11	E12										STD	STD	STD
#K	F1	F2	F3	F4	F5	F6	F7	F8	F9	F10	F11	F12	F1	F2	F3	F4	F5	F6	F7	F8	F9	F10	F11	F12
#L	F1	F2	F3	F4	F5	F6	F7	F8	F9	F10	F11	F12										STD	STD	STD
#M	G1	G2	G3	G4	G5	G6	G7	G8	G9	G10	G11	G12	G1	G2	G3	G4	G5	G6	G7	G8	G9	G10	G11	G12
#N	G1	G2	G3	G4	G5	G6	G7	G8	G9	G10	G11	G12										STD	STD	STD
#O	H1	H2	H3	H4	H5	H6	H7	H8	H9	H10	H11	H12	H1	H2	H3	H4	H5	H6	H7	H8	H9	H10	H11	H12
#P	H1	H2	H3	H4	H5	H6	H7	H8	H9	H10	H11	H12										NTC	NTC	NTC


def add_parameters(parameters):
	parameters.add_int(
		variable_name="mm_volume",
		display_name="Master Mix Volume",
		default=8,
		minimum=1,
		maximum=20,
		description=("What volume should be loaded")
	)
	parameters.add_int(
		variable_name="template_volume",
		display_name="Template Volume",
		default=2,
		minimum=1,
		maximum=20,
		description=("What volume should be loaded")
	)
	parameters.add_int(
		variable_name="ResLocation",
		display_name="Reservoir Location",
		default=4,
		minimum=3,
		maximum=10,
		description=("Where is the reservoir located?")
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
	parameters.add_str(
		variable_name="layout",
		display_name="qPCR Layout",
		default="SideBySide",
		choices=[
			{"display_name": "SideBySide", "value": "SideBySide"},
			{"display_name": "Integra", "value": "Integra"},
			{"display_name": "Legacy", "value": "Legacy"}
		],
		description=("Which layout should qPCR plate be set up with? See layouts in this github folder.")
	)
	parameters.add_str(
		variable_name="platetype",
		display_name="Plate Type",
		default="biorad_96_wellplate_200ul_pcr",
		choices=[
			{"display_name": "Biorad/VWR 96", "value": "biorad_96_wellplate_200ul_pcr"},
			{"display_name": "Qiagen Elution Plate !NOTREADY", "value": "biorad_96_wellplate_200ul_pcr"}
		],
		description=("What type of plate is the DNA in?")
	)


def run(protocol: protocol_api.ProtocolContext):
	
	dnaplate = protocol.load_labware(protocol.params.platetype, '2')
	qPCRplate = protocol.load_labware('biorad_384_wellplate_50ul', '1')
	
	tips1 = protocol.load_labware('opentrons_96_filtertiprack_20ul', '10')
	tips2 = protocol.load_labware('opentrons_96_filtertiprack_20ul', '11')

	reservoir = protocol.load_labware('nest_12_reservoir_15ml', protocol.params.ResLocation)
	mastermix = protocol.deck[protocol.params.ResLocation][protocol.params.MMwell]

	mm_volume=float(protocol.params.mm_volume)
	template_volume=float(protocol.params.template_volume)
	
	# define pipettes
	mp20 = protocol.load_instrument('p20_multi_gen2', 'right', tip_racks=[tips1, tips2])

	if protocol.params.layout == 'SideBySide' or protocol.params.layout == "Legacy":
		dest_wells = [qPCRplate.wells()[i] for i in range(0, 384, 16)] # every 16th number is a new column
		mp20.pick_up_tip()
		mp20.transfer(volume=mm_volume, source=mastermix, dest=dest_wells, new_tip='never')
		dest_wells = [qPCRplate.wells()[i] for i in range(1, 192, 16)] 
		mp20.transfer(volume=mm_volume, source=mastermix, dest=dest_wells, new_tip='never')
		dest_wells = [qPCRplate.wells()[i] for i in range(337, 384, 16)] 
		mp20.transfer(volume=mm_volume, source=mastermix, dest=dest_wells, new_tip='never')
		mp20.drop_tip()

	if protocol.params.layout == 'Integra':
		dest_wells = [qPCRplate.wells()[i] for i in range(0, 384, 16)] # every 16th number is a new column
		mp20.pick_up_tip()
		mp20.transfer(volume=mm_volume, source=mastermix, dest=dest_wells, new_tip='never')
		dest_wells = [qPCRplate.wells()[i] for i in range(1, 384, 32)] 
		mp20.transfer(volume=mm_volume, source=mastermix, dest=dest_wells, new_tip='never')
		dest_wells = [qPCRplate.wells()[i] for i in range(288, 384, 32)] 
		mp20.transfer(volume=mm_volume, source=mastermix, dest=dest_wells, new_tip='never')
		mp20.drop_tip()


	# define the 12 transfers needed for each layout based on the top column using multichanenls. 
	#This is a hash of lists where the key is the 96 well position, and the entries are the target wells.
	
	if protocol.params.layout == 'SideBySide':
		transfers = {
		'A1' : ['A1', 'A2', 'A3'],
		'A2' : ['A4', 'A5', 'A6'],
		'A3' : ['A7', 'A8', 'A9'],
		'A4' : ['A10', 'A11', 'A12'],
		'A5' : ['A13', 'A14', 'A15'],
		'A6' : ['A16', 'A17', 'A18'],
		'A7' : ['A19', 'A20', 'A21'],
		'A8' : ['A22', 'A23', 'A24'],
		'A9' : ['B1', 'B2', 'B3'],
		'A10' : ['B4', 'B5', 'B6'],
		'A11' : ['B7', 'B8', 'B9'],
		'A12' : ['B10', 'B11', 'B12']
		}
		
	if protocol.params.layout == 'Integra':
		transfers = {
		'A1' : ['A1', 'A2', 'B1'],
		'A2' : ['A3', 'A4', 'B3'],
		'A3' : ['A5', 'A6', 'B5'],
		'A4' : ['A7', 'A8', 'B7'],
		'A5' : ['A9', 'A10', 'B9'],
		'A6' : ['A11', 'A12', 'B11'],
		'A7' : ['A13', 'A14', 'B13'],
		'A8' : ['A15', 'A16', 'B15'],
		'A9' : ['A17', 'A18', 'B17'],
		'A10' : ['A19', 'A20', 'B19'],
		'A11' : ['A21', 'A22', 'B21'],
		'A12' : ['A23', 'A24', 'B23']
		}
		
	if protocol.params.layout == 'Legacy':
		transfers = {
		'A1' : ['A1', 'B1', 'A13'],
		'A2' : ['A2', 'B2', 'A14'],
		'A3' : ['A3', 'B3', 'A15'],
		'A4' : ['A4', 'B4', 'A16'],
		'A5' : ['A5', 'B5', 'A17'],
		'A6' : ['A6', 'B6', 'A18'],
		'A7' : ['A7', 'B7', 'A19'],
		'A8' : ['A8', 'B8', 'A20'],
		'A9' : ['A9', 'B9', 'A21'],
		'A10' : ['A10', 'B10', 'A22'],
		'A11' : ['A11', 'B11', 'A23'],
		'A12' : ['A12', 'B12', 'A24']
		}
		
	for source, dests in transfers.items():
		#dest_wells = [qPCRplate.wells()[dests]] # every 16th number is a new column
		mp20.pick_up_tip()
		mp20.aspirate(template_volume*3.2, dnaplate[source]) # pulling an extra 0.6ul for repeated pipetting
		mp20.dispense(template_volume, qPCRplate[dests[0]])
		mp20.dispense(template_volume, qPCRplate[dests[1]])
		mp20.dispense(template_volume, qPCRplate[dests[2]])
		mp20.drop_tip()
