# QIASeq Whole Virome Library Preparation

## Principle and Overview
Due to the diverse nature of viral genomes, it is often difficult to capture the entire virome for shotgun metagenomics. This is because many library preparations for short-read technologies are only specific for dsDNA, as they use bead-linked transposons for this purpose. Other technologies may be able to capture single-stranded DNA templates but will not capture the RNA viruses present within an extract. This QIASeq library preparation is unique in this regard as it allows for the capture of RNA and DNA viruses, as well as single-stranded and double-stranded templates. The protocol can be broken down into the following steps:

- **Converting RNA and ssDNA into double-stranded cDNA**
- **QIASeq FX DNA Library Construction**

This protocol is meant for Illumina sequencing platforms.

## Required Reagents and Equipment

- [ ] 100% ethanol (ACS grade)
- [ ] Agilent 4200 TapeStation
- [ ] Heat Block
- [ ] Ice
- [ ] Magnetic Stand
- [ ] Microcentrifuge
- [ ] Multichannel pipettor
- [ ] Nuclease-Free Water
- [ ] PCR Tubes
- [ ] PCR Workstation
- [ ] QIAseq Beads
- [ ] QIAseq FX DNA Library Core Kit
- [ ] QIAseq UDI Y-Adapter Kit B
- [ ] QIAseq xHYB Box 2
- [ ] Rotator
- [ ] Single-channel pipettor
- [ ] Thermal Cycler
- [ ] Vacuum Concentrator

## Procedure

### 1. Total Nucleic Acid cDNA Synthesis
This step of procedure will perform the following: 1) Random priming for RNA 2) 1st stand cDNA synthesis 3) 2nd strand synthesis 4) QIASeq bead cleanup.

#### 1a. Reagent Preparation

- A range of 10 - 100ng of TNA is recommended for input.
- Prepare fresh 80% ethanol.
- Equilibrate QIASeq Beads to room temperature 30 mins before use.
- Pre-program the thermal cyclers for speed and convience.
- Thaw reagents on ice. Once thawed, vortex thoroughly and quickly spin down.

#### 1b. Reaction Buffer Setup and Thermal Cycler Programming

- [ ] Prepare the reaction buffers according to the number of samples you are processing. Each excess reagent is incorporated to account for pipetting error:

**Random Priming Reaction**
| Component | Per Sample (µL) |
| :--: | :--: |
| Microbial RP | 1.2 |
| BC3 buffer | 2.2 |

**First strand synthesis reaction**
| Component | Per Sample (µL) |
| :--: | :--: |
| RI RNase Inhibitor | 1.2 |
| EZ Reverse Transcriptase | 1.2 |

**Second strand synthesis reaction**
| Component | Per Sample (µL) |
| :--: | :--: |
| Nuclease-free water | 5.2 |
| XC Buffer | 2.2 |
| RH RNase | 1.2 |
| dNTP | 1.2 |
| BX enzyme | 1.2 |

- [ ] Save the following programs into the thermal cycler :

**Random priming reaction**
| Temperature | Time (min) |
| :--: | :--: |
| 65°C | 5 |
| Ice | >2|

**First strand synthesis reaction**
| Temperature (°C) | Time (min) |
| :--: | :--: |
| 25 | 10 |
| 42 | 30 |
| 70 | 15 |
| 4 | Hold |

**Second strand synthesis**
| Temperature (°C)| Time (min) |
| :--: | :--: |
| 37 | 7 |
| 65| 10 |
| 80 | 10 |
| 4 | Hold |

#### 1c.cDNA Reaction

- [ ] Add 5 µL of your TNA sample per well. Add 3 µL of the **Random priming reaction** buffer to each well for a total volume of 8 µL.
- [ ] Mix well by pipetting up and down. Or utilize a plate shaker. Spin down briefly.
- [ ] Incubate the reactions in the pre-programmed thermal cycler for the **Random Priming Reaction**.
- [ ] Once incubated, remove samples from thermal cycler and quickly spin down. Place on ice. Add 2 µL of the **First strand synthesis reaction** buffer to each well. The total reaction volume should be 10 µL.
- [ ] Mix well by pipetting up and down. Or utilize a plate shaker. Spin down briefly.
- [ ] Incubate the reactions in the pre-programmed thermal cycler for the **First strand synthesis reaction**.
- [ ] Once incubated, remove samples from thermal cycler and quickly spin down. Place on ice.
- [ ] Add 10 µL of the **Second strand synthesis reaction** buffer. The total reaction buffer should be 20µL. 
- [ ] Mix well by pipetting up and down. Or utilize a plate shaker. Spin down briefly.
- [ ] Incubate the reactions in the pre-programmed thermal cycler for the **Second strand synthesis reaction**.
- [ ] Once incubated, remove samples from thermal cycler and quickly spin down. Place on ice.

#### 1d. Bead Cleanup
- [ ] Add 30 µL of nuclease-free water to each well. Remove samples from ice.
- [ ] Add 65 µL of QIASeq Beads to each sample. Pipette up and down. Or mix by plate shaker. Spin down briefly.
- [ ] Incubate at room temperature for 5 mins.
- [ ] Place on magnetic stand. Leave on the stand for 5 minutes. Once the solution has cleared remove the supernatant, taking care not to remove the beads from the sample.
- [ ] **Repeat 2x:** Add 200 µL of 80% ethanol to each well while on the magnetic stand. Move the plate side to side in the 2 positions of the magnet to wash the beads. Carefull remove and discard the wash.
- [ ] To ensure that the ethanol has been completely removed, briefly centrifuge and return the plate to the magnetic stand. First using a 200 µL pipette, remove excess ethanol. After, use a 10 µL pipette to remove residual ethanol.
- [ ] With the plate still on the magnet, air-dry at room-temperature for 2-5 minutes.

> [!IMPORTANT]
> Take care not to overdry the beads as you will get lower DNA recovery.

- [ ] Elute in 18.25 µL of nuclease-free water. Thoroughly resuspend the beads off the magnet. Incubate for 1-2 minutes at room temperature. Place on the magnetic rack until teh solution is clear.
- [ ] Transfer 15.75 µL of the eluate into a new plate.
- [ ] Libraries can be safely stored at -20°C.

> [!NOTE]
> DNA can now be quantified with Qubit. This will allow you to determine the optimal cycle number for the library amplification step in the QIAseq FX kit.
 
### 2. QIAseq FX DNA Library Kit

#### 2a. Reagent Preparation

- Equilibrate the QIAseq Beads to room temperature at least 30 minutes before use.
- Ensure that the DNA is in water, 10 mM Tris, or Qiagen's EB Buffer. If there is EDTA, the DNA must be cleaned before proceding into the library preparation.
- Thaw reagents on ice (and DNA if previously frozen) and prepare the reaction buffers **ON ICE** as follows:

**Fragmentation Reaction**
| Component | Per Sample (µL) |
| :--: | :--: |
| FX Buffer, 10x | 2.45 |
| FX Enzyme Mix | 4.7 |

**Ligation Reaction**
| Component | Per Sample (µL) |
| :--: | :--: |
| UPH Ligation Buffer | 20.2 |
| DNA Ligase | 5.2 |

**Library Amplification**
| Component | Per Sample (µL) |
| :--: | :--: |
| HiFi PCR Master Mix | 25.2 |
| Primer Mix | 1.7 |
| Lib Amp Blocker | 1.2 |

#### 2b. Thermal Cycler Programming

**Fragmentation Reaction**
| Temperature (°C) | Time (min) |
| :--: | :--: |
| 4 | 1 |
| 32 | 16 |
| 65 | 30 |
| 4 | Hold |

**Ligation Reaction**
| Temperature (°C) | Time (min) |
| :--: | :--: |
| 20 | 15 |

**Library Reaction**
| Step | Time | Temperature (°C) |
| :--: | :--: | :--: |
| Hold | 2 min | 98 |
| 3 step cycling: | | |
| Step 1 | 20s | 98 |
| Step 2 | 30s | 60 |
| Step 3 | 30s | 72 |
| 14 cycles | | |
| Final Extension | 1 min | 72 |
| Hold | ∞ | 4 |

#### 2c. Library Preparation Procedure
- [ ] Thaw reagents for the **Fragmentation Reaction** and make the stock solutions.
- [ ] Start the fragmentation reaction on the thermal cycler to get the heating block to temperature.
- [ ] Place samples on ice and add the 6.75 µL of the **Fragmentation Reaction** buffer to 15.75 µL of the eluted DNA. Ensure the DNA is kept on ice throughout this process.
- [ ] Pipette up and down 15 times to mix or utilize a plate shaker. Quickly spin down.
- [ ] Place into samples into the pre-chilled thermal cycler and resume the cycling program.
- [ ] Upon completion, remove the samples and place them on ice.
- [ ] **Prior to the termination of the Fragmentation Reaction**: 
	- [ ] Thaw the adapters while the samples are on the thermal cycler.
	- [ ] Prepare the **Adapter Ligation** reaction buffer while the samples are on the thermal cycler.
- [ ] Start the **Ligation Reaction** on the thermal cycler, pausing the program to allow it come to temperature. **Be sure to turn off the heated lid**.
- [ ] With the samples on ice, add 25 µL of the **Ligation Reaction** buffer to each sample.
- [ ] Utilizing the adapter plate, pierce the foil seal and transfer 2.5 µL of one DNA adapter to each sample well.
- [ ] Mix well by pipetting up and down 15 times, or utilize a plate shaker. Briefly spin down.
- [ ] Place the samples in the thermal cycler and incubate.
- [ ] While the samples are on the thermal cycler, equilibrate the QIAseq beads to room temperature. Prepare 80% ethanol. Thaw reagents for the **Library Amplification Reaction** buffer.
- [ ] Upon termination of the program proceed with a bead cleanup:
	- [ ] Add 50 µL of Nuclease-free water to the ligation reaction
	- [ ] Add 90 µL of QIAseq Beads to each sample. Mix by pipetting up and down 10 times. Briefly centrifuge.
	- [ ] Incubate for 5 mins at room temperature.
	- [ ] Place on the magnetic rack for 5 mins, waiting for the solution to have cleared.
	- [ ] Remove the supernatant.
	- [ ] Place on magnetic stand. Leave on the stand for 5 minutes. Once the solution has cleared remove the supernatant, taking care not to remove the beads from the sample.
	- [ ] **Repeat 2x:** Add 200 µL of 80% ethanol to each well while on the magnetic stand. Move the plate side to side in the 2 positions of the magnet to wash the beads. Carefull remove and discard the wash.
	- [ ] To ensure that the ethanol has been completely removed, briefly centrifuge and return the plate to the magnetic stand. First using a 200 µL pipette, remove excess ethanol. After, use a 10 µL pipette to remove residual ethanol.
	- [ ] With the plate still on the magnet, air-dry at room-temperature for 2-5 minutes.
	- [ ] Elute in 52.5 µL of Nuclease-free water. Remove from rack and mix well by pipetting. Incubate at room temperature for 1 -2 minutes.
	- [ ] Place on magnetic rack until the solution clears. 
	- [ ] Transfer 50 µL of the supernatant to a new plate.
	- [ ] Add 55 µL of QIAseq Beads to each sample. Mix by pipetting 10x or by plate shaking. Briefly centrifuge.
	- [ ] Incubate for 5 mins at room temperature.
	- [ ] Place on the magnetic rack for 5 mins, waiting for the solution to have cleared.
	- [ ] Remove the supernatant.
	- [ ] Place on magnetic stand. Leave on the stand for 5 minutes. Once the solution has cleared remove the supernatant, taking care not to remove the beads from the sample.
	- [ ] **Repeat 2x:** Add 200 µL of 80% ethanol to each well while on the magnetic stand. Move the plate side to side in the 2 positions of the magnet to wash the beads. Carefully remove and discard the wash.
	- [ ] To ensure that the ethanol has been completely removed, briefly centrifuge and return the plate to the magnetic stand. First using a 200 µL pipette, remove excess ethanol. After, use a 10 µL pipette to remove residual ethanol.
	- [ ] With the plate still on the magnet, air-dry at room-temperature for 2-5 minutes.
	- [ ] Elute in 25 µL of Nuclease-free water. Remove from the rack and mix by pipetting up and down. Incubate 1 -2 mins. Place on magnetic stand until solution clears.
	- [ ] With the solution clear transfer 22.5 µL of the supernatant to a new plate.
- [ ] Pre-heat the thermal cycler by initiating the **Library Amplification Reaction**.
- [ ] Prepare the **Library Amplification Reaction** buffer.
- [ ] Add 27.5 µL of the **Library Amplification Reaction** buffer to each sample. Mix by pipetting up and down 10 times. Spin down.
- [ ] Transfer the tube to the thermal cycler and start the program.
- [ ] While the program is running, be sure to equilibrate the QIAseq Beads to room temperature. Prepare fresh 80% ethanol.
- [ ] Upon termination of the program, be sure to proceed immediately into the bead cleanup:
	- [ ] Add 55 µL of QIAseq Beads to each sample. Mix by pipetting 10x or by plate shaking. Briefly centrifuge.
	- [ ] Incubate for 5 mins at room temperature.
	- [ ] Place on the magnetic rack for 5 mins, waiting for the solution to have cleared.
	- [ ] Remove the supernatant.
	- [ ] Place on magnetic stand. Leave on the stand for 5 minutes. Once the solution has cleared remove the supernatant, taking care not to remove the beads from the sample.
	- [ ] **Repeat 2x:** Add 200 µL of 80% ethanol to each well while on the magnetic stand. Move the plate side to side in the 2 positions of the magnet to wash the beads. Carefully remove and discard the wash.
	- [ ] To ensure that the ethanol has been completely removed, briefly centrifuge and return the plate to the magnetic stand. First using a 200 µL pipette, remove excess ethanol. After, use a 10 µL pipette to remove residual ethanol.
	- [ ] With the plate still on the magnet, air-dry at room-temperature for 2-5 minutes.
	- [ ] Elute in 27.5 µL of Nuclease-free water. Remove from the rack and mix by pipetting up and down. Incubate 1 -2 mins. Place on magnetic stand until solution clears.
	- [ ] With the solution clear transfer 25 µL of the supernatant to a new plate.









