from opentrons import protocol_api

requirements = {"robotType": "OT-2", "apiLevel": "2.21"}

# metadata
metadata = {
	'protocolName': 'Set up 384-well qPCR from 96 well plate', 
	'author': 'J Bisanz, jordan.bisanz@gmail.com',
	'description': 'Loads master mix from 12-well reservoir to 384 well plates, and then add template from 96 well plate.'
}


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

	if protocol.params.layout == 'SideBySide':
		dest_wells = [qPCRplate.wells()[i] for i in range(0, 384, 16)] # every 16th number is a new column
		mp20.pick_up_tip()
		mp20.transfer(volume=mm_volume, source=mastermix, dest=dest_wells, new_tip='never')
		dest_wells = [qPCRplate.wells()[i] for i in range(1, 192, 16)] 
		mp20.transfer(volume=mm_volume, source=mastermix, dest=dest_wells, new_tip='never')
		dest_wells = [qPCRplate.wells()[i] for i in range(336, 384, 16)] 
		mp20.transfer(volume=mm_volume, source=mastermix, dest=dest_wells, new_tip='never')
		mp20.drop_tip()
