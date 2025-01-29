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


# In Progress:

### 4. Clean Up Libraries

**Theory:** This is a relatively standard bead cleanup using a double sided size selection to remove small fragments such as adapter dimers, and also large fragments that will not cluster efficiently. Care must be taken because in the first bead cleanup, the supernatant is kept, and in the second cleanup, the bound fraction is kept!

**Reagents needed:** IPB = Illumina Purification Beads; RSB = Resuspension Buffer. Thaw at room temperature. Make fresh 80% Ethanol.


Vortex IPB before each use. Pipette slowly.

- [ ] Bring IPB and RSB to room temp
- [ ] Centrifuge at 280 × g for 1minute to collect contents at the bottom of the well.
- [ ] Place the plate on the magnetic stand and wait until the liquid is clear (~5 minutes).
- [ ] Transfer 9 µL supernatant from each well of the PCR plate to the corresponding well of a new Deepwell MIDI plate.
- [ ] Vortex and invert IPB multiple times to resuspend.
- [ ] For standard DNA input, do as follows. If using small amplicon, see Illumina manual.
 + Add 8 µL nuclease-free water to each well containing supernatant.
 + Add 9 µL IPB to each well containing supernatant.
 + Pipette each well 10 times to mix. Alternatively, seal the plate and use a plate shaker at 1600 rpm for 1minute.
 + Seal the plate and incubate at room temperature for 5 minutes.
 + Place on the magnetic stand and wait until the liquid is clear (~5 minutes).
 + During incubation, thoroughly vortex the IPB (undiluted stock tube), and then add 3 µL to each well of a new deepwell MIDI plate.
 + Transfer 25 µL supernatant from each well of the first plate into the corresponding well of the new deepwell MIDI plate containing 3 µL undiluted IPB.
 + Pipette each well in the MIDI plate 10 times to mix. Alternatively, seal the plate and use a plate shaker at 1600 rpm for 1minute.
 + Discard the first plate.
 + Capture the beads and discard the supernatant
 + With the plate on the magnetic stand, add 40 µL fresh 80% EtOH without mixing.
 + Without disturbing the beads, remove and discard supernatant.
 + With the plate on the magnetic stand, add 40 µL fresh 80% EtOH without mixing.
 + Without disturbing the beads, remove and discard supernatant.
- [ ] Remove and discard residual EtOH.
- [ ] Air-dry on the magnetic stand for 5 minutes.
- [ ] Remove from the magnetic stand.
- [ ] Add 15 µL RSB to the beads.
- [ ] Pipette to resuspend.
- [ ] Incubate at room temperature for 2 minutes.
- [ ] Place the plate on the magnetic stand and wait until the liquid is clear (~2 minutes).
- [ ] Transfer 12 µL supernatant to a new 96-well PCR plate.

SAFE STOPPING POINT
If you are stopping, seal the plate and store at -25°C to -15°C for up to 30 days.


### 5. Pool Libraries

When the DNA input is 20-100 ng, quantifying and normalizing individual libraries generated in the same experiment is not necessary. However, the final yield of libraries generated in separate experiments can vary slightly.
To achieve optimal cluster density, pool equal library volumes and quantify the pool before sequencing.

#### For DNA Inputs of 100–500 ng:
- [ ] Combine 1 µL of each library (up to 384 libraries) in a 1.7 ml microcentrifuge tube.
- [ ] Vortex to mix, and then centrifuge.
- [ ] Quantify the library pool using a dsDNA fluorescent dye method, such as Qubit or PicoGreen.


## Check Library Quality (Optional)

Use the tapestation HS screentape assay to ensure insert sizes are of desired size and distribution. (600bp with a range of ~ 150-1500bp)
