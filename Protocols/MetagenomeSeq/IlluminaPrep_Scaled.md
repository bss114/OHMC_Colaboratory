# Illumina DNA Prep

## Theory

This protocol is adapted from Illumina's [DNA Prep protocol](https://support.illumina.com/content/dam/illumina-support/documents/documentation/chemistry_documentation/illumina_prep/illumina-dna-prep-reference-guide-1000000025416-10.pdf), with the main difference that volumes have been scaled down by a factor of 5 in the name of costs. The final bead cleanup is brought up to larger volumes to ensure accurate size selection before drying back down to concentrate. This protocol integrates DNA tagmentation, amplification, cleanup and pooling. Power users can use the following [guide](https://support.illumina.com/content/dam/illumina-support/documents/documentation/chemistry_documentation/illumina_prep/illumina-prep-checklist-1000000033561-06.pdf).

## Materials

### Equipment
- [ ] 96-well AND/OR 384-well plate magnet 
- [ ] Microplate centrifuge (Ex. USA Scientific 2532-2000)
- [ ] Microcentrifuge (Ex. VWR 53283-802)
- [ ] Vortexer (Ex Neta HEATH-120567)
- [ ] Qubit Fluorometer (Fisher 13400525)
- [ ] Tapestation 4200 (Agilent)
- [ ] Thermocycler (Ex. BioRad PTC)
- [ ] Speedvac with plate rotor (optional for concentrating libraries)

### Consumables
- [ ] Illumina DNA Prep Kit (**catalog needed**)
- [ ] Qubit assay tubes (**catalog needed**)
- [ ] Qubit dsDNA HS assay kit (Thermo Q32854)
- [ ] Agilent Highsensitivity D1000 ScreenTape and sample buffer (Agilent 5067-5584 and 5067-5603)
- [ ] Multi and single channel pipettes + tips for 10, 20, 200ul
- [ ] Adhesive and foil seals for 96-well plates (Ex. USA Scientific 2923-0110)
- [ ] 96-well PCR plate (Ex. VWR 82006-704)
- [ ] 1.7mL centrifuge tubes (Ex. VWR 87003-294)

## Protocol

To start, assess input concentration. Dilute all samples to a concentration of 5ng/ul. Note: samples must be free of contaminants such as wash buffer carryover. This can be assessed using the Nanodrop, *but only if the concentration of >50ng/ul*. Final concentration should be measured via Qubit hsDNA. Use of nanodrop to quantify samples <50ng/ul is highly prone to error and *will* result in inaccurate quantification, and potential library failure.

A script is available in the OT2 scripts folder to aid in this purpose: see [here](https://github.com/BisanzLab/OHMC_Colaboratory/tree/main/OT2_scripts/TransferAndDilute). A csv file is provided as a template.

All DNA should be resuspended in water or Tris-HCl. *Avoid EDTA/TE where possible.*

*Note: There is 1 safe stopping point in this protocol after PCR. For all other steps proceed immediately.*

### 1. Tagmentation
**Reagents needed:** BLT = bead-linked transposons  (4˚C); TB1 = tagment buffer 1  (-20˚C). Both at room temperature and vortexed to mix. Do not centrifuge.

Save the following TAG program on the thermal cycler:
* Choose the preheat lid option and set to 100°C
* Set the reaction volume to 10 µL
* 55°C for 15 minutes
* Hold at 10°C

- [ ] Start the TAG program on the thermal cycler and hit pause to preheat the unit.
- [ ] Add 6 µL DNA (5ng/µL) to each well of a 96-well (or 384-well) PCR plate. Be sure to record what sample is in what well for future sequencing. A template is available [here](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Templates/IndexTrackingSheet.xlsx).
- [ ] Vortex BLT vigorously for 10 seconds to resuspend.
- [ ] For each sample to be prepared combine 0.45 µL BLT with 1.75 water in an eppi tube. *Note: this step is to increase fragment size; however, it may be omited depending on the end user's goals*
- [ ] For each sample sample to be prepared add 2.2µL TB1 to prepare the Tagmentation Master Mix in a single tube.
- [ ] Evenly dispense the tagmentation mastermix across a 8-tube strip. **If at any time beads appear to have settled, pipette to mix**.
- [ ] Transfer 4 μl of Tagmentation Master Mix from the 8-tube strip to each well of the plate containing a sample using a multichannel. Pipette 10x to mix. Use fresh tips for each sample column.
- [ ] Seal the plate with an aluminum seal and place on thermocycler. Resume run. When run is complete proceed **immediately** to step 2.

*Note: In storing BLT, make sure beads are always stored upright and submerged in the buffer*

### 2. Post-Tagmentation Cleanup and Amplification
**Reagents needed:**  TSB = tagment stop buffer  (4˚C); TWB = tagment wash buffer (4˚C). Vortex to mix. If TSB contains SDS and will likely precipitate. Heat at 37C until dissolved. PM = Enhanced PCR Mix (-20˚C) thawed on ice. Indexes (-20˚C) thawed on ice **and centrifuged before use***.

This step amplifies cleans up the tagmentation reaction and amplifies the tagmented DNA using a limited-cycle PCR program. The PCR step adds Index 1 (i7) adapters, Index 2 (i5) adapters, and sequences required for sequencing cluster generation. To confirm the indexes selected for low plexity pooling have the appropriate color balance, see the [Index Adapters Pooling Guide](https://support-docs.illumina.com/SHARE/IndexAdaptersPooling/Content/SHARE/FrontPages/IndexAdapterPooling.htm). If sequencing more than ~24 samples, this is not a concern.


Save the following PTC program on the thermal cycler:
* Choose the preheat lid option and set to 100°C
* Set the reaction volume to 12 μl
* 37°C for 15 minutes
* Hold at 10°C

Save the following BLT PCR program on a thermal cycler using the appropriate number of PCR cycles. 8-10 is a good starting point for anticipated input DNA. *Note: you may wish to increase the cycle count if doing lower input DNA*
* Choose the preheat lid option and set to 100°C
* 68°C for 3 minutes
* 98°C for 3 minutes
* (10) cycles of:
 + ---98°C for 45 seconds
 + ---62°C for 30 seconds
 + ---68°C for 2 minutes
* 68°C for 1 minute
* Hold at 10°C

- [ ] Start the PTC program on the thermocycler and hit pause to prehit the unit.
- [ ] Using a multichannel or integra add 2 µL TSB to each well of the plate. Pipette 10x to mix (or use plate vortex giving a quick spin after vortexing).
- [ ] Seal plate and place on the thermal cycler. Resume the PTC program.
- [ ] While PTC program is running, prepare PCR mastermix. For each sample combine 4.4µL of EPM with 4.4µL of water. Dispense evenly across 8-tube strip.
- [ ] **Immediately after the PTC program has finished**, place the plate on the magnetic stand and wait until liquid is clear (~3 minutes).
- [ ] Using a multichannel pipette or Integra, remove and discard supernatant (12 µL) leaving the beads behind with the tagmented DNA.
- [ ] Wash three (3) times as follows. Note: an integera may be used here. Set aspiration speed to 2 when removing supernatants from beads to avoid disturbing pellet:
 + Remove the sample plate from the magnetic stand and use a deliberately slow pipetting technique to add 20 µL TWB directly onto the beads. A deliberately slow pipetting technique minimizes the potential of TWB foaming to avoid incorrect volume aspiration and incomplete mixing.
 + Pipette slowly until beads are fully resuspended.
 + Place the plate on the magnetic stand and wait until the liquid is clear (~3 minutes).
 + Using a multichannel pipette, remove and discard supernatant.  **Note: Beads will dry if left without supernant. Proceed immediately to next step or leave last TWB until ready to proceed.**
- [ ] Remove plate from magnetic.
- [ ] Using multichannel add 8 µL of master mix to each well of plate ensuring that master mix comes into contact with bead pellet.
- [ ] Quickly centrifuge index plate.
- [ ] Using integra remove 2 µL of indexes and add to each well.
- [ ] Pippette 10x to ensure mixing or use plate vortex followed by quick spin.
- [ ] Seal the plate with Microseal 'B', and then centrifuge at 280 × g for 30 seconds.
- [ ] Place on the preprogrammed thermal cycler and run the BLT PCR program.

**SAFE STOPPING POINT**
If you are stopping, store at 2°C to 8°C for up to 30 days.

### 3. Clean Up Libraries

**Theory:** The manual calls for a double sided selection (0.53x right sided, 0.71 left sided); however, our experience has been that this insufficiently removes small fragments in the scaled reaction. Instead this protocol is using two separate 0.7x selections to result in libraries with a peak size in the 500-600 range. This step can be effectively performed using an integra, multichannel, or OT2 with appropriate calibration. **Note: to save on tips, the same tips that are used to add beads/wash, can also be used for elution if left on multi-channel or integra).** This step is best accomplished in a 384-well plate given the small pipetting volumes if using an Integra.

**Reagents needed:** IPB = Illumina Purification Beads; RSB = Resuspension Buffer. Thaw at room temperature. Make fresh 80% Ethanol.

Vortex IPB before each use. Pipette slowly. Residual beads on the side of tips can greatly skew the size selection preventing effective removal of small fragments.

- [ ] Bring IPB and RSB to room temp
- [ ] Centrifuge the PCR products from the previous step at 280 × g for 1minute to collect contents at the bottom of the well
- [ ] Place the plate on the magnetic stand and wait until the liquid is clear (~5 minutes)
- [ ] Transfer 9 µL supernatant from each well of the PCR plate to a new 96-well (or 384-well).
- [ ] To each well, add 6.3 µL of of IPB (0.7x), pipette to mix.
- [ ] Capture beads
- [ ] Using slowest pipette speed, remove 15 µL supernatant and place in discard plate
- [ ] Add 80% Ethanol to the well (120µL if using 96-well plate or 12.5 µL if using 384-well plate). It is not necessary to mix at this stage
- [ ] Capture beads, remove 12.5 µL supernatant and place in discard plate.
- [ ] Add 80% Ethanol to the well (120µL if using 96-well plate or 12.5 µL if using 384-well plate). It is not necessary to mix at this stage
- [ ] Capture beads, remove 12.5 µL supernatant and place in discard plate.
- [ ] Add 12.5 µL µL water to elute beads, mix by pipetting, or with plate vortex. If using a 96-well plate it is essential that water resuspends beads
- [ ] Transfer 12 µL µL eluted DNA to a new 96-well (or 384-well) plate containing 8.4 µL IPB (0.7x)
- [ ] Capture beads
- [ ] Using slowest pipette speed, remove 20.4 µL supernatant and place in discard plate
- [ ] Add 80% Ethanol to the well (120µL if using 96-well plate or 12.5 µL if using 384-well plate). It is not necessary to mix at this stage
- [ ] Capture beads, remove 12.5 µL supernatant and place in discard plate.
- [ ] Add 80% Ethanol to the well (120µL if using 96-well plate or 12.5 µL if using 384-well plate). It is not necessary to mix at this stage
- [ ] Capture beads, remove 12.5 µL supernatant and place in discard plate.
- [ ] Add 12.5 µL RSB to elute beads, mix by pipetting, or with plate vortex. If using a 96-well plate it is essential that water resuspends beads
- [ ] Transfer 11 µL eluate to a new 96 well plate. *Note: it is possible to elute in higher volumes if doing by hand. Higher volume eluates may be dried using speed vac, and resuspended in appropriate volume for downstream analysis*.
- [ ] Store at -20 ˚C until pooling/sequencing.

## QC

Use Tapestation dsDNA HS to evaluate size distribution of libraries. Aming for ~600bp peak size with range of 150-1500bp. Ideally there are no visible adapter dimers <150nt. If these are present, additional cleanup will be required.

