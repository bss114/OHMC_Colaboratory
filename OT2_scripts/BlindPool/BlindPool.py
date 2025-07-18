from opentrons import protocol_api

requirements = {"robotType": "OT-2", "apiLevel": "2.21"}

# metadata
metadata = {
	'protocolName': 'Blind Pool Libraries v0.1', 
	'author': 'J Bisanz, jordan.bisanz@gmail.com',
	'description': 'Loads a fixed volume of every well of a 96 well plate (in deck 1) into a the first column of a new  (deck 2). For iSeq QC runs.'
}


def add_parameters(parameters):
	parameters.add_int(
		variable_name="volume",
		display_name="Pooling Volume",
		default=1,
		minimum=1,
		maximum=5,
		description=("What volume of each sample should be loaded")
	)
	parameters.add_int(
		variable_name="StartingColumn",
		display_name="Starting Column",
		default=1,
		minimum=1,
		maximum=12,
		description=("Which column should loading start at?")
	)
	parameters.add_int(
		variable_name="EndingColumn",
		display_name="Ending Column",
		default=12,
		minimum=1,
		maximum=12,
		description=("Which column should loading end on?")
	)
	parameters.add_int(
		variable_name="TipLocation",
		display_name="Tip Location",
		default=3,
		minimum=3,
		maximum=10,
		description=("Where are the tips located? Assuming a max of 96 samples to be transf.")
	)



#Don't edit below this line unless you want to change the functionality of the script

def run(protocol: protocol_api.ProtocolContext):
	
	LibraryPlate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', 1)
	PoolingPlate = protocol.load_labware('biorad_96_wellplate_200ul_pcr', 2)
	tips = protocol.load_labware('opentrons_96_filtertiprack_20ul', protocol.params.TipLocation)

	mm_volume=float(protocol.params.volume)
	
	# define pipettes
	mp20 = protocol.load_instrument('p20_multi_gen2', 'right', tip_racks=[tips])

	for col in range(protocol.params.StartingColumn, protocol.params.EndingColumn+1):
		mp20.pick_up_tip(tips['A'+str(col)])
		mp20.aspirate(mm_volume, LibraryPlate['A'+str(col)])
		mp20.dispense(mm_volume, PoolingPlate['A'+str(col)])
		mp20.mix(repetitions=2, volume=mm_volume, location=PoolingPlate['A'+str(col)])
		mp20.drop_tip()
