from opentrons import protocol_api

requirements = {"robotType": "OT-2", "apiLevel": "2.21"}

# metadata
metadata = {
	'protocolName': 'Demonstrate and Train on OT2', 
	'author': 'J Bisanz, jordan.bisanz@gmail.com',
	'description': 'Transfers dye from A1 of a 12-well to 384 well plate in selectable pattern for training.',
}


def add_parameters(parameters):
	parameters.add_str(
		variable_name="Pattern",
		display_name="Source Plate Type",
		default="psu",
		choices=[
			{"display_name": "PSU", "value": "psu"},
			{"display_name": "Hello", "value": "hello"},
			{"display_name": "Star", "value": "star"},
		],
		description=("What pattern should be pipetted?")
	)
	parameters.add_int(
		variable_name="PlateLocation",
		display_name="384 Well Plate Location",
		default=1,
		minimum=1,
		maximum=10,
		description=("Where is the eppi tube of diluent located? Assuming in A1 of tube rack.")
	)
	parameters.add_int(
		variable_name="DyeLocation",
		display_name="Dye Location",
		default=2,
		minimum=1,
		maximum=10,
		description=("Where is the 12 well with dye?")
	)
	parameters.add_int(
		variable_name="TipLocation",
		display_name="Tip Location",
		default=3,
		minimum=1,
		maximum=10,
		description=("Where are the tips located? Assuming a max of 96 samples to transfer.")
	)
	parameters.add_int(
		variable_name="Volume",
		display_name="Dye Volume",
		default=2,
		minimum=1,
		maximum=20,
		description=("What volume should be transfered?")
	)
	parameters.add_str(
		variable_name="DyeWell",
		display_name="Dye Well",
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
		description=("Which well of the reservoir contains the dye?")
	)


def run(protocol: protocol_api.ProtocolContext):

	#set up the wells for the pattern choice
	if protocol.params.Pattern == 'psu':
		wells=['B1','B2','B3','B4','B5','B6','B7','B8','B10','B11','B12','B13','B14','B15','B16','B18','B24','C1','C8','C10','C18','C24','D1','D8','D10','D18','D24','E1','E8','E10','E18','E24','F1','F8','F10','F18','F24','G1','G2','G3','G4','G5','G6','G7','G8','G10','G11','G12','G13','G14','G15','G16','G18','G24','H1','H16','H18','H24','I1','I16','I18','I24','J1','J16','J18','J24','K1','K16','K18','K24','L1','L16','L18','L24','M1','M10','M11','M12','M13','M14','M15','M16','M18','M19','M20','M21','M22','M23','M24']
	elif protocol.params.Pattern == 'hello':
		wells=['C1','C3','C5','C6','C7','C9','C13','C17','C18','C19','C20','C22','C23','D1','D3','D5','D9','D13','D17','D20','D22','D23','E1','E3','E5','E9','E13','E17','E20','E22','E23','F1','F2','F3','F5','F6','F7','F9','F13','F17','F20','F22','F23','G1','G3','G5','G9','G13','G17','G20','H1','H3','H5','H9','H13','H17','H20','H22','H23','I1','I3','I5','I6','I7','I9','I10','I11','I13','I14','I15','I17','I18','I19','I20','I22','I23','K2','K3','K4','K5','K6','K7','K8','K9','K10','K11','K12','K13','K14','K15','K16','K17','K18','K19','K20','K21','K22','K23','L3','L4','L5','L6','L7','L8','L9','L10','L11','L12','L13','L14','L15','L16','L17','L18','L19','L20','L21','L22','M4','M5','M6','M7','M8','M9','M10','M11','M12','M13','M14','M15','M16','M17','M18','M19','M20','M21','N5','N6','N7','N8','N9','N10','N11','N12','N13','N14','N15','N16','N17','N18','N19','N20','O6','O7','O8','O9','O10','O11','O12','O13','O14','O15','O16','O17','O18','O19','P7','P8','P9','P10','P11','P12','P13','P14','P15','P16','P17','P18']
	elif protocol.params.Pattern == 'star':
		wells=['A5','A20','B4','B5','B6','B19','B20','B21','C1','C2','C3','C4','C5','C6','C7','C8','C9','C16','C17','C18','C19','C20','C21','C22','C23','C24','D2','D3','D4','D5','D6','D7','D8','D17','D18','D19','D20','D21','D22','D23','E3','E4','E5','E6','E7','E18','E19','E20','E21','E22','F3','F4','F6','F7','F18','F19','F21','F22','G3','G7','G18','G22','J12','K11','K12','K13','L8','L9','L10','L11','L12','L13','L14','L15','L16','M9','M10','M11','M12','M13','M14','M15','N10','N11','N12','N13','N14','O10','O11','O13','O14','P10','P14']

	plate = protocol.load_labware('biorad_384_wellplate_50ul', protocol.params.PlateLocation)
	dye = protocol.load_labware('nest_12_reservoir_15ml', protocol.params.DyeLocation)
	tips = protocol.load_labware('opentrons_96_filtertiprack_20ul', protocol.params.TipLocation)
	p20 = protocol.load_instrument('p20_single_gen2','left',tip_racks=[tips])

	p20.pick_up_tip()
	for well in wells:
		p20.aspirate(float(protocol.params.Volume), dye['A1'])
		p20.dispense(float(protocol.params.Volume), plate[well])
	p20.drop_tip()