#UNDER CONSTRUCTION


# Illumina DNA Prep - High Throughput

## Theory

This protocol uses the [Illumina DNA Prep protocol](https://support.illumina.com/content/dam/illumina-support/documents/documentation/chemistry_documentation/illumina_prep/illumina-dna-prep-reference-guide-1000000025416-10.pdf); however, reaction volumes have been scaled for cost savings, and all steps are performed on 96 samples simultaneously. Also, to aid in cost reductions, optional substitutions of some illumina reagents are included which may facilitate higher throughput processing. Broadly speaking, this library step involves 4 steps:

1) Tagmentation: in this step, DNA becomes bound to magnetic beads and an enzymatic process shears the DNA while leaving handles that will allow for subsequent amplification and indexing. The reaction takes place on a thermocycler and is stopped by the addition of SDS (buffer TSB). The protocol must continue to step 2 immediately on completion.

2) Cleanup and PCR: beads carrying DNA are captured using magnets and the tagmentation reagents are removed. A PCR mastermix is then added to the beads which will release the DNA from the beads. Sample-specific index primers are then added before a limited-cycle PCR is performed. This makes more library, as well as adds the sample-specific indexes that allow the samples to be mixed and sequenced in a single pool. The protocol may be paused after this step.

3) Size Selection: In this step, the PCR reagents are removed while simultaneously removing small fragments and adapter dimers that may cause issues in downstream sequencing. In this protocol size selection is accomplished via two 0.7X size selections. The resulting libraries are then eluted in a 10 mM Tris-HCl pH 8.5 buffer with 0.1% Tween 20 (buffer RSB) for subsequent QC and sequencing. The protocol may be paused after this step.

4) QC: Some (or all) libraries are analyzed for size distribution using an Agilent Tapestation to ensure appropriate size distribution and yield.

**Sample Input Requirements**: All samples must be pure DNA free of contaminants such as organic solvents or wash buffers from extraction. It is anticipated that most DNA has been derived from the QIAcube HT Powersoil kit which should not have these issues. Samples should be pre-normalized to 5 ng/ul and have at least 15 µL available. To normalize the samples, they should be measured by qubit (if yield of samples is <30ng/ul), or Nanodrop (if sample yield is >=30ng/ul). **If using Nanodrop, the 260/230 ratio must be over 1.4.** Samples must be in a fully skirted 96 well plate to begin. The 5ng/ul samples in a 96 well plate may be prepared by hand, or with the aid of a script in the OT2 scripts folder of this repository [here](https://github.com/BisanzLab/OHMC_Colaboratory/tree/main/OT2_scripts/TransferAndDilute). A CSV template is provided.

***

## Change log
- v0.1_June2025: Initial testing and optimization, under construction
  
***

## Step 1: Tagmentation

### 1.1 Equipment
- [ ] 384-well thermocycler: suggested to use QIAquant 384 in co-lab
- [ ] 12.5 µL Integra mini-96
- [ ] 10 µL multi-channel pipette (Suggested Gilson P8x10L)
- [ ] Plate centrifuge (Suggested USA Sci 2532-2000)

### 1.2 Consumables
- [ ] Illumina bead linked transposon (BLT) - warmed to room temperature
- [ ] Illumina tagmentation buffer (TB1) - on ice
- [ ] 0.5 boxes of 12.5 µL Integra grip tips (Cat #6405)
- [ ] 1 x 384 well plate (Suggested Armadillo PCR Plate, Thermo Cat# AB3384)
- [ ] 0.1 x 96 tip box of 10 µL pipette tips with barriers compatible with manual multi-channel pipette
- [ ] Plate seals (suggested to use Biorad Microplate B seals Cat# MSB1001)
- [ ] Generic multichannel reservoirs (Suggested VWR 53504-035)

### 1.3 Protocol

#### Preparation

**gDNA Plate:** Ensure DNA is thawed in 96 well plate. This plate should ideally have at least 15 µL of gDNA at 5 ng/µL to allow for at least 2 passes in the event of error. Plate should be centrifuged before opening.

**BLT:** These are the bead linked transposons. **It is imperative that they are not placed in the freezer or stored on ice.** 

**TSB Plate:** If not already prepared, transfer 25 µL of TSB to each well of a 96 well plate. This can be used for multiple runs.

**Tagmentation Plate:** In a multichannel reservoir, combine 220 µL of well-mixed beads (BLT) with 220 µL tagmentation buffer (TB1). Mix well and use 10 µL multi channel to transfer 4 µL of mixture into every other column/row of a 384 well plate. **Note:** because this protocol uses multichannels and Integra mini-96s, the spacing needs to be every other well. This has the advantage of also putting an empty well between every sample which may be advantageous from a cross-contamination standpoint. It is theoretically possible to do up to 384 well samples at a time; however, this is not recommended. In effect, using your 8 channel in a vertical orientation, put the first tip into the following wells to fill the plate: A1, A3, A5, A7, A9, A11, A13, A15, A17, A19, A21, A23.

#### Procedure
- [ ] Using 12.5 µL Integra, use the **TAG LOAD** program to transfer 6µL from the gDNA plate to the Tagmentation plate and mix
- [ ] Cover with plate seal
- [ ] Briefly centrifuge the plate
- [ ] Transfer to preheated thermocycler running program **TAG** (*see thermocycler program appendix*)
- [ ] After TAG cycle, briefly centrifuge and remove seal
- [ ] Using the 12.5 µL Integra, use the **TAG STOP** program to transfer 2 µL from the TSB plate to the tagmentation plate and mix.
- [ ] Cover with plate seal
- [ ] Briefly centrifuge the plate
- [ ] Transfer to preheated thermocycler running program **PTC**
- [ ] Immediately proceed to Step 2. It may be beneficial to do step 2 preparations while PTC runs.

***

## Step 2: Cleanup and PCR

### 2.1 Equipment
- [ ] 384-well thermocycler: suggested to use QIAquant 384 in co-lab
- [ ] 12.5 µL Integra mini-96
- [ ] 125 µL Integra mini-96
- [ ] 10 µL multi-channel pipette (Suggested Gilson P8x10L)
- [ ] Plate centrifuge (Suggested USA Sci 2532-2000)
- [ ] 384-well magnetic capture plate (Suggested Permagen Thomas Sci Cat# 23A00H882)

### 2.2 Consumables
- [ ] Illumina Tagmentation Wash Buffer (TWB) - at room temperature
- [ ] Illumina Enhanced PCR Mastermix (EPM) - on ice
- [ ] Illumina Indexes (or Co-lab indexes, see substitutions) - 
- [ ] Nuclease free water
- [ ] Nuclease free 1.5 mL microcentrifuge tube
- [ ] 1-well reservoir (Suggested Opentrons 999-00078)
- [ ] 200 µL PCR strip tube
- [ ] 0.25 boxes of 12.5 µL Integra grip tips (Cat #6405) 
- [ ] 0.75 boxes of 125 µL Integra grip tips (Cat #6465) 
- [ ] 1 tip box of 10 µL pipette tips with barriers compatible with manual multi-channel pipette
- [ ] Plate seals (suggested to use Biorad Microplate B seals Cat# MSB1001)

### 2.3 Protocol

#### Preparation

**TWB Plate:** If not previously done, using a generic reservoir and multichannel distribute 200 µL TWB to each well of a 96 well plate. This will be used for multiple runs.

**PCR Master Mix:** In a nuclease free tube, combine 420 µL EPM with 420 µL nuclease free water. Transfer 110 µL into each tube in a 8-tube PCR strip tube. Store strip on ice.

**Index Plate:** Thaw on ice. To prevent potential issues with cross contamination, it is essential these plates are briefly centrifuged before being opened. The seal must be immediately discarded and replaced with a fresh seal.


#### Procedure
*Note:* In this procedure the beads cannot be allowed to dry. Work quickly any time the beads are not in solution.
- [ ] Briefly centrifuge the tagmentation plate
- [ ] Remove seal and transfer tagmentation plate to 384-well magnet
- [ ] Capture beads (will take approximately 2 minutes)
- [ ] Using the 12.5 µL Integra, discard the supernatant. *Settings: Asp volume: 12.5, Asp speed: 1*
- [ ] Using the custom program **TWB Wash** on the 125 µL Integra, conduct **first** wash with TWB:
	- [ ] Remove tagmentation plate from magnet
	- [ ] Aspirate 20 µL from TWB Reservoir
	- [ ] Dispense and mix 10x in tagmentation plate
	- [ ] Cover 384-well plate using plate lid, briefly centrifuge
	- [ ] Capture beads on magnet (approximately 2 minutes)
	- [ ] Aspirate 20 µL supernatant and discard
	- [ ] Eject tips
- [ ] Using the custom program **TWB Wash** on the 125 µL Integra, conduct **second** wash with TWB:
	- [ ] Remove tagmentation plate from magnet
	- [ ] Aspirate 20 µL from TWB Plate.
	- [ ] Dispense and mix 10x in tagmentation plate
	- [ ] Cover 384-well plate using plate lid, briefly centrifuge
	- [ ] Capture beads on magnet (approximately 2 minutes)
	- [ ] Aspirate 20 µL supernatant and discard being sure not to cross contaminate tips
	- [ ] **DO NOT** Eject tips
- [ ] Cover 384-well plate using plate lid, briefly centrifuge
- [ ] Use 125 µL Integra with program **FINAL DRY** to remove residual TWB
- [ ] Working **very** quickly to prevent beads from drying, use 10 µL multichannel to add 8µL of the PCR Master Mix to each well. Briefly mix by pipetting to ensure beads are resuspended in Master Mix.
- [ ] Cover 384-well plate using plate lid, briefly centrifuge
- [ ] Using 12.5 µL Integra, use the **BLT INDEX** program to transfer 2 µL from the Index Plate to the tagmentation plate and mix
- [ ] Cover with plate seal. **Note: a good seal is imperative to prevent evaporation. Great care should be taken to ensure this is not a problem.**
- [ ] Briefly centrifuge the plate
- [ ] Transfer to preheated thermocycler running program **BLT PCR** (*see thermocycler program appendix*)
- [ ] After BLT PCR, either proceed, or store at -20˚C.

***

## Step 3: Size Selection

### 3.1 Equipment
- [ ] 125 µL Integra mini-96
- [ ] Plate centrifuge (Suggested USA Sci 2532-2000)
- [ ] 10 µL multi-channel pipette (Suggested Gilson P8x10L)
- [ ] 384-well magnetic capture plate (Suggested Permagen Thomas Sci Cat# 23A00H882)

### 3.2 Consumables
- [ ] 100% EtOH
- [ ] Illumina Purificaiton Beads (IPB) - at room temperature
- [ ] Illumina Resuspension Buffer (RSB) - at room temperature
- [ ] Nuclease free water
- [ ] 2 x 1-well reservoir (Suggested Opentrons 999-00078) 
- [ ] 1.75 boxes of 125 µL Integra grip tips (Cat #6465)
- [ ] 0.2 x 96 tip box of 10 µL pipette tips with barriers compatible with manual multi-channel pipette
- [ ] Plate seals (suggested to use Biorad Microplate B seals Cat# MSB1001)
- [ ] Generic multichannel reservoirs (Suggested VWR 53504-035)
- [ ] 96 well plate (Suggested VWR 82006-704)
- [ ] 2 x 384 well plates (Suggested Armadillo Fisher Cat# AB3384)

### 3.3 Protocol

#### Preparation

**EtOH Reservoir:** Mix 50mL of fresh 80% Ethanol (40 mL 100% EtOH, 10 mL nuclease-free water). Transfer to 1-well reservoir.

**Water Reservoir:** Transfer enough nuclease free water to a 1-well reservoir with enough to cover all wells.

**Size Selection Plate 1:** Mix IPB well and pour into a 50mL reservoir. Using 10 µL multichannel transfer **6.3 µL IPB** (0.7X) into each well corresponding to the tagmentation plate. Cover this plate with a plate lid. Good pipetting practice is essential here to obtain correct bead ratios. Use a repeated dispensing approach: Aspirate and discard beads back into reservoir leaving plunger depressed to first stop. Aspirate beads and dispense in receiver plate. Do not use blow stop. Repeat.

**Size Selection Plate 2:** Mix IPB well and pour into a 50mL reservoir. Using 10 µL multichannel transfer **8.4 µL IPB** (0.7X) into each well corresponding to the tagmentation plate. Cover this plate with a plate lid. Use pipetting strategy described above.

#### Procedure
- [ ] Briefly centrifuge the tagmentation plate
- [ ] Remove seal and transfer tagmentation plate to 384-well magnet
- [ ] Capture beads (will take approximately 2 minutes)
- [ ] Using 125 µL Integra, use the **IPB LOAD** program to recapture the DNA on IPB Beads:
	- [ ] Transfer 9 µL of superantant from the tagmentation plate to the Size Selection 1 plate and mix
 	- [ ] Incubate 5 min @ room temperature
	- [ ] Capture beads on magnet (approximately 2 minutes)
	- [ ] Aspirate 15.3 µL supernatant and discard
	- [ ] Eject tips
- [ ] Using the custom program IPB Wash on the 125 µL Integra, conduct **first** wash of the **first size selection**:
	- [ ] Aspirate 30 µL from Ethanol Reservoir
	- [ ] Dispense and mix 10x in Size Selection plate on magnet
	- [ ] Cover 384-well plate using plate lid, briefly centrifuge
	- [ ] Capture beads on magnet (approximately 2 minutes)
	- [ ] Aspirate 30 µL supernatant and discard
	- [ ] Eject tips
- [ ] Using the custom program IPB Wash on the 125 µL Integra, conduct **second** wash of the **first size selection**:
	- [ ] Aspirate 30 µL from Ethanol Reservoir
	- [ ] Dispense and mix 10x in Size Selection plate  on magnet
	- [ ] Cover 384-well plate using plate lid, briefly centrifuge
	- [ ] Capture beads on magnet (approximately 2 minutes)
	- [ ] Aspirate 30 µL supernatant and discard
	- [ ] **DO NOT** Eject tips
- [ ] Use 125 µL Integra to collect any residual EtOH with custom program Final Dry
- [ ] Discard tips
- [ ] Air dry plate 5 minutes at room temperature
- [ ] Using 125 µL Integra with the custom program IPB Transfer, elute and transfer to **Size selection plate 2**:
	- [ ] Aspirate 15 µL from Water Reservoir
	- [ ] Dispense and mix in **Size selection plate 1** off magnet
	- [ ] Cover 384-well plate using plate lid, briefly centrifuge
	- [ ] Incubate 5 minutes at room temperature
	- [ ] Capture beads on magnet (approximately 2 minutes)
	- [ ] Aspirate 12 µL superantant from **Size selection plate 1**
	- [ ] Dispense and mix in **Size selection plate 2** off magnet
	- [ ] Discard tips
- [ ] Cover 384-well plate using plate lid, briefly centrifuge
- [ ] Incubate 5 minutes at room temperature to capture DNA
- [ ] Using the custom program IPB Wash on the 125 µL Integra, conduct **first** wash of the **second size selection**:
	- [ ] Aspirate 30 µL from Ethanol Reservoir
	- [ ] Dispense and mix 10x in Size Selection plate  on magnet
	- [ ] Cover 384-well plate using plate lid, briefly centrifuge
	- [ ] Capture beads on magnet (approximately 2 minutes)
	- [ ] Aspirate 30 µL supernatant and discard
	- [ ] Eject tips
- [ ] Using the custom program IPB Wash on the 125 µL Integra, conduct **second** wash of the **second size selection**:
	- [ ] Aspirate 30 µL from Ethanol Reservoir
	- [ ] Dispense and mix 10x in Size Selection plate  on magnet
	- [ ] Cover 384-well plate using plate lid, briefly centrifuge
	- [ ] Capture beads on magnet (approximately 2 minutes)
	- [ ] Aspirate 30 µL supernatant and discard
	- [ ] **DO NOT** Eject tips
- [ ] Use 125 µL Integra to collect any residual EtOH with custom program Final Dry
- [ ] Discard tips
- [ ] Air dry plate 5 minutes at room temperature
- [ ] Use 125 µL Integra with custom program IPB Elute to elute final libraries:
	- [ ] Aspirate 20 µL from Water Reservoir
	- [ ] Dispense and mix 10x in Size Selection plate 2
	- [ ] Cover 384-well plate using plate lid, briefly centrifuge
	- [ ] Capture beads on magnet (approximately 2 minutes)
	- [ ] Aspirate 17 µL to a new 96 well plate.
- [ ] Label plate as final libraries including project name, date, and name.
- [ ] Freeze at -20˚C or proceed to QC
	
***

## Step 4: QC
	
### 4.1 Equipment
- [ ] 2 µL single channel pipette (suggested Gilson P2L)
- [ ] Tapestation 4200 or equivalent
- [ ] Plate Vortex (comes with Tapestation)
- [ ] Strip tube centrifuge (Suggested Fisher Cat# 02-112-305)

### 4.2 Consumables
- [ ] HSD1000 Screen Tape (Agilent Cat# 5067-5584)
- [ ] HSD1000 Sample Buffer (Agilent Cat# 5067-5603)
- [ ] Tapestation optical tubes (Agilent Cat# 401428)
- [ ] Tapestation caps for optical tubes (Agilent Cat# 401425)
- [ ] Tapestation Loading Tips (Agilent Cat# 5067-5599)
- [ ] Generic barrier tips for 2 µL pipette

### 4.3 Protocol
- [ ] Randomly select 8 samples from plate, or pick important controls and/or potentially problematic samples.
- [ ] In each tube of optical strip tube, put 2 µL of sample buffer
- [ ] Add 2 µL of completed library
- [ ] Add caps, vortex for the automatic time period, and centrifuge for 1 minute
- [ ] Run on tape station using electronic ladder. Be sure to load sample names ahead of time
- [ ] In analysis program you are looking for an average size from ~500-600 nt, with an integrated area from ~400-700 of at least 1nM.
- [ ] Check for presense of dimers (~150 nt), if there is a peak here, an additional cleanup of the pooled libraries may be required.

***

## Appendix 1: Thermocycler programs

**TAG (TAGmentation)**: Reaction volume to 10µL

|Step         | Temperature | Time         |
|-------------|-------------|--------------|
|Tagmentation | 55˚C        | 15 minutes   |
|Hold         | 10˚C        | Infinity     |

**PTC (Tagmentation Stop)**: Reaction volume to 12µL

|Step              | Temperature | Time         |
|------------------|-------------|--------------|
|Tagmentation Stop | 37˚C        | 15 minutes   |
|Hold              | 10˚C        | Infinity     |



**PTC (Tagmentation Stop)**: Reaction volume to 10µL

|Step                 | Temperature | Time         |
|---------------------|-------------|--------------|
|Activation           | 68˚C        | 3 minutes    |
|Initial denaturation | 98˚C        | 3 minutes    |
|12 cycles\*:
|----->Denature       | 98˚C        | 45 seconds   |
|----->Anneal         | 62˚C        | 30 seconds   |
|----->Extend         | 68˚C        | 2 minutes    |
|Final extension      | 68˚C        | 1 minute     |
|Hold                 | 10˚C        | Infinity     |

*Note:* cycle count can be adjusted based on input. It is not recommended to go above this cycle count unless working on extremely low biomass samples.


## Appendix 2: Optional Substitutions and Modifications

**Buffer TB1**: This may be replaced by a 20 mM Tris pH 7.6, 20 mM MgCl2, 20% DMF solution. In this case the reaction volumes would be adjusted as this is a 2x tagmentation buffer. rather than a 5x buffer as supplied. To make 1 mL of home-made 2x tagmentation buffer, combine 20 µL 1M Tris-HCl pH 7.5 with 800 µL 25mM MgCl2 (can be stolen from Kappa PCR kits), and 200 µL DMF.

**Buffer TSB**: This may be replaced by a 0.2% SDS solution. Can purchase molecular grade 10% SDS from Sigma (Cat 71736-100mL) and dilute 50x for working solution. This can be advantageous if using 1-well reservoirs for transfers.

**Buffer BLT**: It is possible to dilute BLT in nuclease free water from 1:5 to 1:50. This may aid in throughput and increase fragment size a potential risk of reducing library complexity.

**Buffer TWB**: This may be replaced by a TE-buffer with 10% PEG 8000 and 0.25M NaCl. To make resuspend 4g PEG 8000 and 0.58g NaCl in 40mL TE buffer. Filter with 0.22 µM filter.

**Illumina Indexes:** Depending on desired throughput, it is possible to use co-lab indexes which are a shared resource allowing for up to 574 samples to be sequenced together. These indexes are based on the Illumina indexes.

**Illumina Purification Beads**: These may in theory be replaced with any bead for magnetic capture of DNA; however, the size selection performance should be validated ahead of time. A recipe for home-made capture beads is available [here](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/Misc/DIY_SPRIBeads.md).

**Bead Ratios:** The final output size of the library can be tuned here. The original protocol calls for a double-sided selection; however, we found that two left sided selections better suited our needs after scaling. If a right sided selection is required, it can be done after the fact on the pool.

## Appendix 3: Integra programs

-Under construction

