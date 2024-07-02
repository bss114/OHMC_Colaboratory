# Illumina DNA Prep

## Theory

This protocol is adapted from Illumina's [DNA Prep protocol](https://support.illumina.com/content/dam/illumina-support/documents/documentation/chemistry_documentation/illumina_prep/illumina-dna-prep-reference-guide-1000000025416-10.pdf), with the main difference that volumes have been scaled down by a factor of 5 in the name of costs. This protocol integrates DNA tagmentation, amplification, cleanup and pooling. Power users can use the following [guide](https://support.illumina.com/content/dam/illumina-support/documents/documentation/chemistry_documentation/illumina_prep/illumina-prep-checklist-1000000033561-06.pdf).

## Materials

### Equipment
- [ ] 96-well plate magnet
- [ ] Microplate centrifuge
- [ ] Microcentrifuge
- [ ] Vortexer
- [ ] Qubit Fluorometer
- [ ] Tapestation (optional for QC)
- [ ] Thermocycler

### Consumables
- [ ] Illumina DNA Prep Kit
- [ ] Qubit assay tubes
- [ ] Qubit dsDNA HS assay kit
- [ ] Multi and single channel pipettes + tips for 10, 20, 200, and 1000 uL
- [ ] Adhesive and foil seals for 96-well plates
- [ ] 96-well PCR plate
- [ ] 1.7mL centrifuge tubes
- [ ] 96-well deepwell plate

## Protocol

To start, assess input size. For microbial DNA 0.2-100ng will work. If there's <20ng it will be necessary to quantify the amount to adjust the number of PCR cycles as necessary.

Safe stop points are marked in this protocol. Unless at a safe stop point, move on to the next step immediately.

### Tagmentation
BLT = bead-linked transposons; TB1 = tagment buffer 1.

Save the following TAG program on the thermal cycler:
* Choose the preheat lid option and set to 100°C
* Set the reaction volume to 10 µL
* 55°C for 15 minutes
* Hold at 10°C

- [ ] Bring BLT and TB1 to room temp and vortex. Do not centrifuge.
- [ ] Add 0.4–6 µL DNA to each well of a 96-well PCR plate so that the total input amount is 20–100 ng.
- [ ] If DNA volume < 6 µL, add nuclease-free water to the DNA samples to bring the total volume to 6 µL.
- [ ] Vortex BLT vigorously for 10 seconds to resuspend. Repeat as necessary.
- [ ] Combine 2.2µL of BLT and 2.2µL of TB1 to prepare the Tagmentation Master Mix. Multiply each volume by the number of samples being processed.
- [ ] Vortex the Tagmentation Master Mix thoroughly to resuspend.
- [ ] Divide the Tagmentation Master Mix volume equally into an 8-tube strip.
- [ ] Transfer 4 μl Tagmentation Master Mix from the 8-tube strip to each well of the plate containing a sample. Use fresh tips for each sample column.
- [ ] Discard the 8-tube strip after the Tagmentation Master Mix has been dispensed.
- [ ] Pipette each sample 10 times to resuspend.
- [ ] Seal and place on the preprogrammed thermal cycler and run the TAG program.

In storing BLT, make sure beads are always stored upright and submerged in the buffer

### Post-Tagmentation Cleanup
TSB = tagment stop buffer; TWB = tagment wash buffer

Save the following PTC program on the thermal cycler:
* Choose the preheat lid option and set to 100°C
* Set the reaction volume to 12 μl
* 37°C for 15 minutes
* Hold at 10°C

If ever beads are aspirated into pipette tips, dispense back into the plate on the magnetic stand and wait until the liquid is clear (~2 minutes).

- [ ] IF TSB has precipitated, heat at 37C for 10 minutes, then vortex until dissolved.
- [ ] Add 2 µL TSB to the plate.
- [ ] Slowly pipette each well 10 times to resuspend the beads, and then seal.
- [ ] Seal and place on the preprogrammed thermal cycler and run the PTC program.
- [ ] Place the plate on the magnetic stand and wait until liquid is clear (~3 minutes). Keep on the magnetic stand until told to remove.
- [ ] Using a multichannel pipette, remove and discard supernatant.
- [ ] Wash two times as follows:
 + Remove the sample plate from the magnetic stand and use a deliberately slow pipetting technique to add 20 µL TWB directly onto the beads. A deliberately slow pipetting technique minimizes the potential of TWB foaming to avoid incorrect volume aspiration and incomplete mixing.
 + Pipette slowly until beads are fully resuspended.
 + Place the plate on the magnetic stand and wait until the liquid is clear (~3 minutes).
 + Using a multichannel pipette, remove and discard supernatant.
- [ ] Remove the plate from the magnetic stand and use a deliberately slow pipetting technique to add 20 µL TWB directly onto the beads.
- [ ] Pipette each well slowly to resuspend the beads.
- [ ] Seal the plate and place on the magnetic stand until the liquid is clear (~3 minutes). Keep on the magnetic stand until instructed to remove in the next section.

The TWB remains in the wells to prevent overdrying of the beads.

### Amplify Tagmented DNA
This step amplifies the tagmented DNA using a limited-cycle PCR program. The PCR step adds Index 1 (i7) adapters, Index 2 (i5) adapters, and sequences required for sequencing cluster generation. To confirm the indexes selected for low plexity pooling have the appropriate color balance, see the [Index Adapters Pooling Guide](https://support-docs.illumina.com/SHARE/IndexAdaptersPooling/Content/SHARE/FrontPages/IndexAdapterPooling.htm)

EPM = Enhanced PCR Mix

About Reagents:
* Index adapter plates
 + A well may contain > 10 µL of index adapters.
 + Do not add samples to the index adapter plate.
 + Each well of the index plate is single use only.
* Index adapter tubes
 + Open only one index adapter tube at a time to prevent misplacing caps. Alternatively, use fresh caps after opening each tube.

Indexing tips:
* Illumina DNA Prep is compatible with IDT for Illumina DNA/RNA Unique Dual (UD), IDT for Illumina Nextera DNA Unique Dual (UD), and Nextera DNA Combinatorial Dual (CD) Indexes.
* Pipette slowly to minimize foaming.
* Each index plate is for single use only.
* IDT for Illumina DNA/RNA UD Indexes use 10 base pair index codes that differ from Nextera DNA CD indexes, which use eight base pair index codes. Confirm that your sequencing system is configured for 10 base pair index codes.
* Centrifuge at 1000 × g for 1minute to settle liquid away from the seal.
* [< 96 samples] Pierce the foil seal on the index adapter plate using a new pipette tip for each well for only the number of samples being processed.
* [96 samples] Align a new Eppendorf 96-well PCR plate above the index adapter plate and press down to puncture the foil seal on all 96 wells. Press down slowly to avoid tipping the volume over.
* Discard the empty Eppendorf plate used to puncture the foil seal.


Save the following BLT PCR program on a thermal cycler using the appropriate number of PCR cycles, indicated in the table below:
* Choose the preheat lid option and set to 100°C
* 68°C for 3 minutes
* 98°C for 3 minutes
* (X) cycles of:
 + 98°C for 45 seconds
 + 62°C for 30 seconds
 + 68°C for 2 minutes
* 68°C for 1 minute
* Hold at 10°C

** BELOW TABLE REMAINS UNSCALED**

| Total DNA Input (ng) | Number of PCR Cycles (X) |
|----------------------|--------------------------|
| 1–9                  | 12                       |
| 10–24                | 8                        |
| 25–49                | 6                        |
| 50–99                | 5                        |
| 100–500              | 5                        |


- [ ] Thaw EPM on ice. Invert to mix, then briefly centrifuge.
- [ ] Thaw Index adapters at room temperature. If in tubes, vortex and briefly centrifuge. If in plates, spin briefly before use.
- [ ] Combine 4.4µL of EPM and 4.4µL of nuclease-free water to prepare the PCR Master Mix. Multiply each volume by the number of samples being processed.
Reagent overage is included in the volume to ensure accurate pipetting.
- [ ] Vortex, and then centrifuge the PCR Master Mix at 280 × g for 10 seconds.
- [ ] With the plate on the magnetic stand, remove and discard supernatant. Foam that remains on the well walls does not adversely affect the library.
- [ ] Remove from the magnet.
- [ ] Immediately add 8 µL PCR Master Mix directly onto the beads in each sample well.
- [ ] Immediately pipette to mix until the beads are fully resuspended. Alternatively, seal the plate and use a plate shaker at 1600 rpm for 1 minute.
- [ ] Seal the sample plate and centrifuge at 280 × g for 3 seconds.
- [ ] Add the appropriate index adapters to each sample.
 + 1µL of i5 and 1µL of i7 adapters in individual tubes for 24 plex kit
 + 2µL of pre-prepaired i5 and i7 index adapters mix into a 96-well plate for 96 plex kit
- [ ] Using a pipette set to 8 µL, pipette 10 times to mix. Alternatively, seal the plate and use a plate shaker at 1600 rpm for 1minute.
- [ ] Seal the plate with Microseal 'B', and then centrifuge at 280 × g for 30 seconds.
- [ ] Place on the preprogrammed thermal cycler and run the BLT PCR program.

SAFE STOPPING POINT
If you are stopping, store at 2°C to 8°C for up to 30 days.

### Clean Up Libraries

IPB = Illumina Purification Beads; RSB = Resuspension Buffer

Vortex IPB before each use. Pipette slowly.

- [ ] Bring IPB and RSB to room temp
- [ ] Centrifuge at 280 × g for 1minute to collect contents at the bottom of the well.
- [ ] Place the plate on the magnetic stand and wait until the liquid is clear (~5 minutes).
- [ ] Transfer 9 µL supernatant from each well of the PCR plate to the corresponding well of a new Deepwell MIDI plate.
- [ ] Vortex and invert IPB multiple times to resuspend.
- [ ] For standard DNA input, do as follows.
 + Add 8 µL nuclease-free water to each well containing supernatant.
 + Add 9 µL IPB to each well containing supernatant.
 + Pipette each well 10 times to mix. Alternatively, seal the plate and use a plate shaker at 1600 rpm for 1minute.
 + Seal the plate and incubate at room temperature for 5 minutes.
 + Place on the magnetic stand and wait until the liquid is clear (~5 minutes).
 + During incubation, thoroughly vortex the IPB (undiluted stock tube), and then add 3 µL to each well of a new deepwell MIDI plate.
 + Transfer 25 µL supernatant from each well of the first plate into the corresponding well of the new deepwell MIDI plate containing 3 µL undiluted IPB.
 + Pipette each well in the MIDI plate 10 times to mix. Alternatively, seal the plate and use a plate shaker at 1600 rpm for 1minute.
 + Discard the first plate.
- [ ] For small PCR amplicon input, perform the following steps.
 + Add 16.2 µL IPB to each well of the MIDI plate containing supernatant.
 + Pipette each well 10 times to mix. Alternatively, seal the plate and use a plate shaker at 1600 rpm for 1 minute.
- [ ] Incubate the sealed MIDI plate at room temperature for 5 minutes.
- [ ] Place on the magnetic stand and wait until the liquid is clear (~5 minutes).
- [ ] Without disturbing the beads, remove and discard supernatant.
- [ ] Wash two times as follows.
 + With the plate on the magnetic stand, add 40 µL fresh 80% EtOH without mixing.
 + Incubate for 30 seconds.
 + Without disturbing the beads, remove and discard supernatant.
- [ ] Remove and discard residual EtOH.
- [ ] Air-dry on the magnetic stand for 5 minutes.
- [ ] Remove from the magnetic stand.
- [ ] Add 6.4 µL RSB to the beads.
- [ ] Pipette to resuspend.
- [ ] Incubate at room temperature for 2 minutes.
- [ ] Place the plate on the magnetic stand and wait until the liquid is clear (~2 minutes).
- [ ] Transfer 6 µL supernatant to a new 96-well PCR plate.

SAFE STOPPING POINT
If you are stopping, seal the plate and store at -25°C to -15°C for up to 30 days.


### Pool Libraries

When the DNA input is 20-100 ng, quantifying and normalizing individual libraries generated in the same experiment is not necessary. However, the final yield of libraries generated in separate experiments can vary slightly.
To achieve optimal cluster density, pool equal library volumes and quantify the pool before sequencing.

#### For DNA Inputs of 100–500 ng:
- [ ] Combine 1 µL of each library (up to 384 libraries) in a 1.7 ml microcentrifuge tube.
- [ ] Vortex to mix, and then centrifuge.
- [ ] Quantify the library pool using a dsDNA fluorescent dye method, such as Qubit or PicoGreen.

#### For DNA Inputs of < 100 ng:
- [ ] Quantify each library individually using Qubit or PicoGreen.

### Check Library Quality (Optional)

Use the tapestation to ensure insert sizes are of desired size and distribution. (600bp with a range of ~ 150-1500bp)


### Dilute Libraries to the Starting Concentration
** NUMBERS BELOW REMAIN UNSCALED**

This step dilutes libraries to the starting concentration for your sequencing system and is the first step in a serial dilution. After diluting to the starting concentration, libraries are ready to be denatured and diluted to the final loading concentration.
For sequencing, Illumina recommends the read lengths indicated on the Illumina DNA Prep Product Compatibility support site page.
IDT for Illumina DNA/RNA UD Indexes uses 10 base pair index codes that differ from the Nextera DNA CD Indexes , which use eight base pair index codes. This change in base pair index codes can require adjustments to your sequencing run set up.

- [ ] Calculate the molarity value of the library or pooled libraries using the following formula. Use 600 bp as the average library size, or whatever it was found to be in QC.
Molarity = (ng/µL) / (600g/mol * 600bp)
- [ ] Using the molarity value, calculate the volumes of RSB and library needed to dilute libraries to the starting concentration for your system.
| Sequencing System                             | Starting Concentration (nM) | Final Loading Concentration (pM)                        |   |   |
|-----------------------------------------------|-----------------------------|---------------------------------------------------------|---|---|
| HiSeq 2500 and HiSeq 2000 (high output modes) | 2                           | 12                                                      |   |   |
| HiSeq 2500 (rapid run mode)                   | 2                           | 8.5                                                     |   |   |
| HiSeq X, HiSeq 4000, and HiSeq 3000           | 2-3                         | 200-300                                                 |   |   |
| iSeq 100                                      | 2                           | 200                                                     |   |   |
| MiniSeq                                       | 2                           | 1.2-1.3                                                 |   |   |
| MiSeq (v3 reagents)                           | 4                           | 12                                                      |   |   |
| NextSeq 550 and NextSeq 500                   | 2                           | 1.2-1.3                                                 |   |   |
| NextSeq 2000                                  | 2                           | 750                                                     |   |   |
| NovaSeq 6000                                  | 2                           | See document #1000000019358 (NovaSeq 6000 System Guide) |   |   |

- [ ] Dilute libraries using RSB:
 + Libraries quantified as a multiplexed library pool — Dilute the pool to the starting concentration for your system.
 + Libraries quantified individually—Dilute each library to the starting concentration for your system. Add 10 µL of each diluted library to a tube to create a multiplexed library pool.
- [ ] Follow the denature and dilute instructions for your system to dilute to the final loading concentration.
 + For the iSeq 100 System, see the system guide for dilution instructions (libraries are automatically denatured).
 + For the NovaSeq 6000 System, see the system guide for pool and denature instructions.
 + For the HiSeq 4000 and HiSeq 3000 Systems, see the cBot 2 or cBot system guide for reagent preparation instructions.
 + For all other systems, see the denature and dilute libraries guide.

The final loading concentrations are a starting point and general guideline. Optimize concentrations for your workflow and quantification method over subsequent sequencing runs or by flow cell titration.
