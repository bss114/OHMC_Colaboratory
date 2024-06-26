# Library QC by D1000 ScreenTape Assay

## Theory
The Agilent TapeStation is an automated platform for fast and sensitive electrophoresis. The D1000 ScreenTape assay is ideal for the reliable sample QC of libraries in the next-generation sequencing (NGS) workflow as well as PCR and qPCR products. Accurate sizing from 35 – 1,000 bp can be assessed from only 1ul of sample in just a few minutes.

## Materials

- [ ] D1000 ScreenTape (Agilent 50675582, stored at 4C)
- [ ] D1000 Ladder and Sample Buffer (Agilent 5067-5583, stored at 4C)
- [ ] TapeStation loading tips (Agilent 5067*5599)
- [ ] Optical tube 8X strip (Agilent 401428) with cap (401425)


## Protocol
- [ ] Allow D1000 Sample buffer and ladder to equilibrate at room temperature for 30 min.
- [ ] During this time, set up the instrument. Launch the TapeStation Controller software.
- [ ] Flick the ScreenTape device, note the channels that have been already used, and insert it into the slot with the barcode facing back. The software will tell you if it is inserted incorrectly because it won't be able to read the barcode. The barcode will also tell the instrument which channels have been used.
- [ ] In the TapeStation software, select the sample positions for the number of tubes you are analyzing. The number of tips required will be displayed.
- [ ] Vortex reagents and samples, spin down. 
- [ ] Aliquot 3ul D1000 sample buffer in position A1 tube, add 1ul D1000 ladder. Alternatively if you don't have the ladder you can select the electronic ladder in the software.
- [ ] Aliquot 3ul D1000 sample buffer per sample tube. Add 1ul sample to it's respective tube.
- [ ] Apply caps (or seal if 96w plate). Vortex 2000rpm, 1 min.
- [ ] Spin down samples and ladder.

## QC
A successful amplification curve should had formed for all samples, and no curves should be observed for negative controls (**Figure 2**). Optionally, a 1% agarose gel can be used to spot check some amplifications. Sporadic failures can be diluted 10x and attempted again which will correct issues encountered with potential wash buffer carry over.

## Figures

![fig1](https://github.com/jbisanz/AmpliconSeq/blob/master/images/ampcurves.png)

**Figure 2**. qPCR amplification curves for a single sample shows dilution series. Note that the extraction blanks have not amplified. Amplification may be observed at 25 cycles of PCR due to primer dimers in negative controls. See protocols for low biomass samples for more information and recommendations.

## Tables


**Table 3. Primary PCR Amplification Parameters**
Cycle                   |    	Temperature (˚C)     | Time
------------------------|----------------------------|------
Initial Denaturation    |	95	                     | 5 min
23 cycles\*:
Denature                | 98˚C                       | 20 sec
Anneal                  | 55˚C	                     | 15 sec
Extend                  | 72˚C                       | 60 sec
Holding	                | 4˚C	Hold                 | 0 sec


