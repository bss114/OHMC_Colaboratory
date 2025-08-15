# Illumina DNA Prep - Strip Tubes

## Use Case

This protocol is a derived from the high throughput protocol and is intended for users with a limited number of samples where it does not make sense to use a 96-well plate format and instead can do 1 or more samples in strip tubes. It may also be useful to catch samples which failed iSeq QC. **Note: If a Co-Lab user is doing this protocol, it is imperative that they arrange their indexes ahead of time and get aliquots from Bethany. This protocol will not create enough material for NovaSeq sequencing on < 50 samples and must be pooled with other projects.**

## Theory

This protocol uses the [Illumina DNA Prep protocol](https://support.illumina.com/content/dam/illumina-support/documents/documentation/chemistry_documentation/illumina_prep/illumina-dna-prep-reference-guide-1000000025416-10.pdf); however, reaction volumes have been scaled for cost savings, and all steps should be performed on samples simultaneously in strip tibes using a multichannel pipettor. Also, to aid in cost reductions, optional substitutions of some illumina reagents are included which may facilitate higher throughput processing. Broadly speaking, this library step involves 4 steps:

1) Tagmentation: in this step, DNA becomes bound to magnetic beads and an enzymatic process shears the DNA while leaving handles that will allow for subsequent amplification and indexing. The reaction takes place on a thermocycler and is stopped by the addition of SDS (buffer TSB). The protocol must continue to step 2 immediately on completion.

2) Cleanup and PCR: beads carrying DNA are captured using magnets and the tagmentation reagents are removed. A PCR mastermix is then added to the beads which will release the DNA from the beads. Sample-specific index primers are then added followed by a limited-cycle PCR. This makes more library, as well as adds the sample-specific indexes that allow the samples to be mixed and sequenced in a single pool. The protocol may be paused after this step.

3) Size Selection: In this step, the PCR reagents are removed while simultaneously removing small fragments and adapter dimers that may cause issues in downstream sequencing. The resulting libraries are then eluted in for subsequent QC and sequencing. The protocol may be paused after this step.

4) QC: Some (or all) libraries are analyzed for size distribution using an Agilent Tapestation to ensure appropriate size distribution and yield.

**Sample Input Requirements**: All samples must be pure DNA free of contaminants such as organic solvents or wash buffers from extraction. It is anticipated that most DNA has been derived from the QIAcube HT Powersoil kit which should not have these issues. Samples should be pre-normalized to 5 ng/ul and have at least 15 µL available. To normalize the samples, they should be measured by qubit (if yield of samples is <30ng/ul), or Nanodrop (if sample yield is >=30ng/ul). **If using Nanodrop, the 260/230 ratio must be over 1.4.** All DNA should be resuspended in water or Tris-HCl. *Avoid EDTA/TE where possible.*

## Theory

This protocol is adapted from Illumina's [DNA Prep protocol](https://support.illumina.com/content/dam/illumina-support/documents/documentation/chemistry_documentation/illumina_prep/illumina-dna-prep-reference-guide-1000000025416-10.pdf), with the main difference that volumes have been scaled down by a factor of 5 in the name of costs.

## Materials

### Equipment
- [ ] Strip tubes (Ex. VWR 76468-978)
- [ ] 96-well plate magnet compatible with strips (Ex. Thermo 12331D)
- [ ] Strip centrifuge (Ex. Neta OHS-30134157)
- [ ] Microcentrifuge (Ex. VWR 53283-802)
- [ ] Vortexer (Ex Neta HEATH-120567)
- [ ] Qubit Fluorometer (Fisher 13400525)
- [ ] Tapestation 4200 (Agilent)
- [ ] Thermocycler (Ex. BioRad PTC)

### Consumables
- [ ] Illumina DNA Prep Kit (Cat # 20060059)
- [ ] Co-Lab unique dual indexes aliquot (or Illumina Cat 20091654)
- [ ] Qubit assay tubes (Thermo Q32856)
- [ ] Qubit dsDNA HS assay kit (Thermo Q32854)
- [ ] Agilent Highsensitivity D1000 ScreenTape and sample buffer (Agilent 5067-5584 and 5067-5603)
- [ ] Multi and single channel pipettes + tips for 10, 20, 200ul
- [ ] Adhesive and foil seals for 96-well plates (Ex. USA Scientific 2923-0110)
- [ ] 1.7mL centrifuge tubes (Ex. VWR 87003-294)
- [ ] Generic multichannel reservoirs (Suggested VWR 53504-035)

***

## Change log
- v0.1_July2025 JB: Initial rewrite of HTP protocol.
  
***



## Protocol

## Step 1: Tagmentation

### 1.1 Consumables
- [ ] Illumina bead linked transposon (BLT) - warmed to room temperature. **Note: BLT is not to be stored on ice**
- [ ] Illumina tagmentation buffer (TB1) - on ice
- [ ] 200 µL PCR strip tube
- [ ] Nuclease free 1.5 mL microcentrifuge tube
- [ ] 10 µL tips


### 1.2 Protocol

- [ ] For each sample to be prepared, combine 2.2µL of TB1 and 2.2 µL of BLT in a microcentrifuge tube.
- [ ] Transfer 4 µL of the TB1/BLT mixture to strip tube
- [ ] Working quickly, add 6 µL of gDNA to each tube in the strip. Pipette 10x to mix.
- [ ] Briefly centrifuge strip tube
- [ ] Transfer to preheated thermocycler running program **TAG** (*see thermocycler program appendix*)
- [ ] After TAG cycle, briefly centrifuge
- [ ] Working quickly, transfer 2 µL from the TSB plate to the tagmentation tubes. Pipette 10x to mix.
- [ ] Briefly centrifuge
- [ ] Transfer to preheated thermocycler running program **PTC**
- [ ] Immediately proceed to Step 2. It may be beneficial to do step 2 preparations while PTC runs.

***

## Step 2: Cleanup and PCR

### 2.1 Consumables
- [ ] Illumina Tagmentation Wash Buffer (TWB) - at room temperature
- [ ] Illumina Enhanced PCR Mastermix (EPM) - on ice
- [ ] Indexes - on ice
- [ ] Nuclease free water
- [ ] Nuclease free 1.5 mL microcentrifuge tube
- [ ] 200 µL PCR strip tube
- [ ] 10 µL tips
- [ ] 200 µL tips

### 2.3 Protocol

#### Preparation

**PCR Master Mix:** In a nuclease free tube, combine 4.4 µL of EPM with 4.4 µL nuclease free water per library prep. If doing a larger number of samples, divide between a strip tube to allow multichannel usage. Storage on ice


#### Procedure
*Note:* In this procedure the beads cannot be allowed to dry. Work quickly any time the beads are not in solution.
- [ ] Briefly centrifuge
- [ ] Capture beads on magnet (will take approximately 2 minutes)
- [ ] Remove and discard superantant
- [ ] First wash: Add 20 µL of TWB, pipette to mix (off magnet)
- [ ] Briefly centrifuge
- [ ] Capture beads (will take approximately 2 minutes)
- [ ] Remove and discard superantant
- [ ] Second wash: Add 20 µL of TWB, pipette to mix (off magnet)
- [ ] Briefly centrifuge
- [ ] Capture beads (will take approximately 2 minutes)
- [ ] Remove and discard supernatant
- [ ] Working **very** quickly to prevent beads from drying, add 8µL of the PCR Master Mix to each tube. Briefly mix by pipetting to ensure beads are resuspended in Master Mix.
- [ ] Transfer 2 µL of corresponding index to each well and mix by pipetting
- [ ] Briefly centrifuge, ensure there are no bubbles
- [ ] Transfer to preheated thermocycler running program **BLT PCR** (*see thermocycler program appendix*)
      	<br>*Note: 6 cycles is recommended for ~30ng input DNA. For some applications such as virome, increasing cycles may be required up to 12 cycles. This may decrease fragment sizes from 500-600 to ~400-450. The decision should be made with care depending on user's needs.*
- [ ] After BLT PCR, either proceed, or store at -20˚C.

***

## Step 3: Size Selection

### 3.1 Consumables
- [ ] 100% EtOH
- [ ] Illumina Purification Beads (IPB) - at room temperature
- [ ] Nuclease free water
- [ ] 3x 200 µL PCR strip tube
- [ ] 10 µL tips
- [ ] 200 µL tips
- [ ] Generic multichannel reservoirs (Suggested VWR 53504-035)

### 3.2 Protocol

#### Preparation

**EtOH Reservoir:** In a nuclease free tube, mix the required volume of fresh 80% Ethanol (~500 µL/sample). If doing >4 samples, transfer to reservoir.

**Size Selection Strip 1:**  Resuspend IPB well. In a microcentrifuge tube, combine 46µL nuclease free water and 29.7 µL IPB per sample. Transfer 69 µL to each well of a strip tube for the requried number of samples.

**Size Selection Strip 2:** Resuspend IPB well. In a strip tube, add 6 µL of IPB for each sample to be prepared.  This step may be tuned depending on desired size selection. Can also use 5 µL (0.65x), 7 µL (0.69x), 8 µL (0.71x), or 9 µL (0.73x). Illumina specifies 0.73x but this has given suboptimal performance in scaled format. Good pipetting practice is essential here to obtain correct bead ratios. Ensure that any beads adhered to outside of pipette are not added to well.


#### Procedure
- [ ] Briefly centrifuge
- [ ] Capture beads on magnet (~ 2 minutes)
- [ ] Transfer 9 µL from each tube, to the 69 µL IPB/water in **Size Selection Strip 1**. Pipette to mix.
- [ ] Incubate at room temp for 5 minutes.
- [ ] Capture beads on magnet. *Target DNA is now in the supernatant with large mass DNA adhered to the beads*.
- [ ] Transfer 75 µL from **Size Selection Strip 1** to **Size Selection Strip 2** off magnet. Pipette to mix.
- [ ] Incubate at room temp for 5 minutes.
- [ ] Capture beads on magnet. *Target DNA is now adhered to the beads small DNA in the supernatant*.
- [ ] Discard supernatant
- [ ] Wash 2x by adding 200 µL 80% Ethanol, it is not necessary to mix the beads and they can be left captured on the magnet
- [ ] Briefly centrifuge and remove any remaining ethanol using a P2 pipettor
- [ ] Air dry for 2 minutes
- [ ] Add 25 µL of nuclease free water (or Illumina RSB) to elute DNA off magnet. Pipette to mix.
- [ ] Briefly centrifuge.
- [ ] Incubate 2 minutes at room temperature
- [ ] Capture beads on magnet
- [ ] Transfer 20 µL supernatant containing library to new strip tube.
- [ ] Label strip tube including project name, date, and name.
- [ ] Freeze at -20˚C or proceed to QC
	
***

## Step 4: QC
	
### 4.1 Consumables
- [ ] HSD1000 Screen Tape (Agilent Cat# 5067-5584)
- [ ] HSD1000 Sample Buffer (Agilent Cat# 5067-5603)
- [ ] Tapestation optical tubes (Agilent Cat# 401428)
- [ ] Tapestation caps for optical tubes (Agilent Cat# 401425)
- [ ] Tapestation Loading Tips (Agilent Cat# 5067-5599)

### 4.2 Protocols
- [ ] For the number of libraries prepared, put 2 µL of Sample buffer in the corresponding tube of the optical strip tube.
- [ ] Add 2 µL of each library to the corresponding tube.
- [ ] Add caps, vortex on the IKA for the automatic time period (1 minute), and centrifuge for 1 minute
- [ ] Run on tape station using electronic ladder. Be sure to load sample names ahead of time
- [ ] In analysis program you are looking for an average size from ~500-600 nt, with an integrated area from ~400-800 of at least 1nM.
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



**BLT PCR**: Reaction volume to 10µL

|Step                 | Temperature | Time         |
|---------------------|-------------|--------------|
|Activation           | 68˚C        | 3 minutes    |
|Initial denaturation | 98˚C        | 3 minutes    |
|6 cycles\*:
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

**Bead Ratios:** The final output size of the library can be tuned here. This protocol is using a 0.68 for the left side selection which is lower than the original protocol. Can also do multiple left side ratios, or skip right side.
