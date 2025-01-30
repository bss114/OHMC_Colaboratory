# Illumina DNA Prep

## Theory

This protocol is adapted from Illumina's [DNA Prep protocol](https://support.illumina.com/content/dam/illumina-support/documents/documentation/chemistry_documentation/illumina_prep/illumina-dna-prep-reference-guide-1000000025416-10.pdf), with the main difference that volumes have been scaled down by a factor of 5 in the name of costs. The final bead cleanup is brought up to larger volumes to ensure accurate size selection before drying back down to concentrate. This protocol integrates DNA tagmentation, amplification, cleanup and pooling. Power users can use the following [guide](https://support.illumina.com/content/dam/illumina-support/documents/documentation/chemistry_documentation/illumina_prep/illumina-prep-checklist-1000000033561-06.pdf).

## Materials

### Equipment
- [ ] 96-well plate magnet
- [ ] Microplate centrifuge
- [ ] Microcentrifuge
- [ ] Vortexer
- [ ] Qubit Fluorometer
- [ ] Tapestation (optional for QC)
- [ ] Thermocycler
- [ ] Speedvac with plate rotor

### Consumables
- [ ] Illumina DNA Prep Kit (**catalog needed**)
- [ ] Qubit assay tubes (**catalog needed**)
- [ ] Qubit dsDNA HS assay kit (**catalog needed**)
- [ ] Multi and single channel pipettes + tips for 10, 20, 200, and 1000 uL
- [ ] Adhesive and foil seals for 96-well plates (**catalog needed**)
- [ ] 96-well PCR plate (**catalog needed**)
- [ ] 1.7mL centrifuge tubes (**catalog needed**)

## Protocol

To start, assess input concentration. Dilute all samples to a concentration of 5ng/ul. *Note: if needing to adjust a large number of samples, there is an OT2 script for this purpose in the repository.*
All DNA should be free of impurities and resuspended in water or Tris-HCl. Avoid EDTA/TE where possible.
Safe stop points are marked in this protocol. Unless at a safe stop point, move on to the next step immediately.

### 1. Tagmentation
**Reagents needed:** BLT = bead-linked transposons; TB1 = tagment buffer 1. Both at room temperature and vortexed to mix. Do not centrifuge.

Save the following TAG program on the thermal cycler:
* Choose the preheat lid option and set to 100°C
* Set the reaction volume to 10 µL
* 55°C for 15 minutes
* Hold at 10°C

- [ ] 6 µL DNA (5ng/µL) to each well of a 96-well PCR plate.
- [ ] Vortex BLT vigorously for 10 seconds to resuspend.
- [ ] For each sample: combine 2.2µL of BLT and 2.2µL of TB1 to prepare the Tagmentation Master Mix in a single tube. \**Note: This volume includes 10% extra volume for reagent waste.*
- [ ] Vortex the Tagmentation Master Mix thoroughly to resuspend.
- [ ] Divide the Tagmentation Master Mix volume equally into an 8-tube strip. \**Note: This only applies if doing >8 samples.*
- [ ] Transfer 4 μl Tagmentation Master Mix from the 8-tube strip to each well of the plate containing a sample using a multichannel. Use fresh tips for each sample column.
- [ ] Discard the 8-tube strip after the Tagmentation Master Mix has been dispensed.
- [ ] Pipette each sample 10 times to resuspend.
- [ ] Seal and place on the preprogrammed thermal cycler and run the TAG program.

In storing BLT, make sure beads are always stored upright and submerged in the buffer

### 2. Post-Tagmentation Cleanup
**Reagents needed:**  TSB = tagment stop buffer; TWB = tagment wash buffer. Vortex to mix. If TSB has precipitated heat at 37C for 10 minutes.

Save the following PTC program on the thermal cycler:
* Choose the preheat lid option and set to 100°C
* Set the reaction volume to 12 μl
* 37°C for 15 minutes
* Hold at 10°C

If ever beads are aspirated into pipette tips, dispense back into the plate on the magnetic stand and wait until the liquid is clear (~2 minutes).

- [ ] Add 2 µL TSB to the plate.
- [ ] Slowly pipette each well 10 times to resuspend the beads, and then seal.
- [ ] Place on the preprogrammed thermal cycler and run the PTC program.
- [ ] Place the plate on the magnetic stand and wait until liquid is clear (~3 minutes).
- [ ] Using a multichannel pipette, remove and discard supernatant leaving the beads behind with the tagmented DNA.
- [ ] Wash three (3) times as follows:
 + Remove the sample plate from the magnetic stand and use a deliberately slow pipetting technique to add 20 µL TWB directly onto the beads. A deliberately slow pipetting technique minimizes the potential of TWB foaming to avoid incorrect volume aspiration and incomplete mixing.
 + Pipette slowly until beads are fully resuspended.
 + Place the plate on the magnetic stand and wait until the liquid is clear (~3 minutes).
 + Using a multichannel pipette, remove and discard supernatant.  **Note: Unless immediately adding PCR master mix, leave the beads in the final 20 µL TWB to avoid drying.**

The TWB remains in the wells to prevent overdrying of the beads.

### 3. Amplify Tagmented DNA
This step amplifies the tagmented DNA using a limited-cycle PCR program. The PCR step adds Index 1 (i7) adapters, Index 2 (i5) adapters, and sequences required for sequencing cluster generation. To confirm the indexes selected for low plexity pooling have the appropriate color balance, see the [Index Adapters Pooling Guide](https://support-docs.illumina.com/SHARE/IndexAdaptersPooling/Content/SHARE/FrontPages/IndexAdapterPooling.htm)

**Reagents needed:** EPM = Enhanced PCR Mix. Indexes. Thaw on ice.

Save the following BLT PCR program on a thermal cycler using the appropriate number of PCR cycles, indicated in the table below. *Note: you may wish to increase the cycle count if doing lower input DNA*
* Choose the preheat lid option and set to 100°C
* 68°C for 3 minutes
* 98°C for 3 minutes
* (10) cycles of:
 + ---98°C for 45 seconds
 + ---62°C for 30 seconds
 + ---68°C for 2 minutes
* 68°C for 1 minute
* Hold at 10°C

- [ ] Thaw EPM on ice. Invert to mix, then briefly centrifuge.
- [ ] Thaw Index adapters at room temperature. **It is essential to briefly spin the plate down before opening.**
- [ ] For each sample, combine 4.4µL of EPM and 4.4µL of nuclease-free water to prepare the PCR Master Mix. 
- [ ] Vortex, and then centrifuge the PCR Master Mix at 280 × g for 10 seconds.
- [ ] With the plate on the magnetic stand, remove and discard TWB supernatant. Foam that remains on the well walls does not adversely affect the library.
- [ ] Remove from the magnet.
- [ ] Immediately add 8 µL PCR Master Mix directly onto the beads in each sample well.
- [ ] Immediately pipette to mix until the beads are fully resuspended. Alternatively, seal the plate and use a plate shaker at 1600 rpm for 1 minute.
- [ ] Seal the sample plate and centrifuge at 280 × g for 3 seconds.
- [ ] Add 2µL of the appropriate index adapters to each sample.
- [ ] Using a pipette set to 8 µL, pipette 10 times to mix. Alternatively, seal the plate and use a plate shaker at 1600 rpm for 1minute.
- [ ] Seal the plate with Microseal 'B', and then centrifuge at 280 × g for 30 seconds.
- [ ] Place on the preprogrammed thermal cycler and run the BLT PCR program.

SAFE STOPPING POINT
If you are stopping, store at 2°C to 8°C for up to 30 days.

### 4. Clean Up Libraries

**Theory:** This is a relatively standard bead cleanup using a double sided size selection to remove small fragments such as adapter dimers, and also large fragments that will not cluster efficiently. Care must be taken because in the first bead cleanup, the supernatant is kept, and in the second cleanup, the bound fraction is kept!

**Reagents needed:** IPB = Illumina Purification Beads; RSB = Resuspension Buffer. Thaw at room temperature. Make fresh 80% Ethanol.

Vortex IPB before each use. Pipette slowly.

- [ ] Bring IPB and RSB to room temp
- [ ] Centrifuge the PCR products from the previous step at 280 × g for 1minute to collect contents at the bottom of the well
- [ ] Place the plate on the magnetic stand and wait until the liquid is clear (~5 minutes)
- [ ] Transfer 9 µL supernatant from each well of the PCR plate to the corresponding well of a 96 well plate
- [ ] Add 42 µL nuclease water to each well
- [ ] Add 27 µL IPB to each well (0.53x). Ensure that beads are well mixed
- [ ] Pipette 10x to mix
- [ ] Capture beads
- [ ] While beads are being captured, transfer 9 µL of IPB to each well of a new plate (0.12x)
- [ ] Transfer 75 µL supernatant from the captured beads, to the new plate containing 9 µL beads
- [ ] Pipette 10x to mix
- [ ] Capture beads and discard supernants
- [ ] Wash with 120 µL 80% EtOH, capture beads, and discard supernatant
- [ ] Wash with 120 µL 80% EtOH, capture beads, and discard supernatant
- [ ] Ensure all trace EtOH has been removed from the wells using fine pipette tips if necessary
- [ ] Add 35 µL nuclease-free water to each well and pipette to mix
- [ ] Capture beads
- [ ] Transfer 30 µL nuclease free water to a new 96 well plate
- [ ] Vacufuge with the settings V-AQ at 30˚C until dry (approximately X min)
- [ ] Add 12 ul to each well, and use plate vortex for 1 minute to ensure that DNA has been resuspended
- [ ] Freeze at -20˚C.

## QC

Use Tapestation dsDNA HS to evaluate size distribution of libraries. Aming for ~600bp peak size with range of 150-1500bp. Ideally there are no visible adapter dimers <150nt. If these are present, additional cleanup will be required.

