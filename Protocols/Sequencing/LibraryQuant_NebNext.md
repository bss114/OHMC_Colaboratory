# NEB Next Quant Kit for Illumina

## Theory
The NEBNext Library Quant Kit is a qPCR-based quantitation method for libraries prepared for Illumina NGS platforms. Library quantitation is critical for proper cluster generation on the Illumina flow cell.  This kit contains primers which target the P5 and P7 Illumina adaptor sequences and a set of high-quality, pre-diluted DNA standards to enable reliable quantitation of diluted DNA libraries between 150–1000 bp.

## Materials

- [ ] New England Biolabs E7630S
- [ ] Nuclease-free water
- [ ] PCR plate + seal


## Protocol
***Location:** PCR hood or separate room/area from other steps; clean benchtop is fine*
- [ ] Wipe pipettes and work areas with DNaseAway or similar, treat PCR area with UV light for ~15 minutes.
### Reagent preparation
Thaw the following reagents on ice:
- [ ] Master Mix
- [ ] 20X Primer Mix
- [ ] DNA standards (tubes 1-6)
- [ ] 10X Dilution buffer
Vortex briefly and do a quick spin, keep reagents on ice.

- [ ] If first time using the kit, add 100ul 20X primer mix to the tube of Master Mix. Vortex 10 sec and indicate on the tube that the primers have been added, and the date. Keep on ice.
      
- [ ] Dilute the 10X  Dilution Buffer 1:10 with nuclease-free water. Vortex 10 sec. Prepare sufficient buffer for the desired number of libraries to be quantitated, allowing 1.3 ml for each library (including NTC). If using a multichannel pipet, allow more volume for loss.

### Prepare library dilutions in low binding tubes:
- [ ] add 1ul library to 999ul of 1X dilution buffer to create a 1:1000 dilution, mix.
- [ ] add 10ul of the 1:1000 to 90ul of 1X dilution buffer to create a 1:10,000 dilution, mix.
- [ ] add 10ul of the 1:10,000 to 90ul of 1X dilution buffer to create a 1:100,000 dilution, mix.

### Prepare qPCR
- [ ] Aliquot 16ul Master Mix containing primers into a 384w PCR plate. This can be done with a multichannel pipet, however keep in mind that Master Mix+primers is a limiting reagent.
It is recommended to run samples in triplicate. For quantitating one library, you will need 9 wells for library dilutions, 3 wells for the no template controls (NTC), and 18 wells for DNA standards.
- [ ] Add 4ul into each respective well for each DNA standard, NTC (use 4ul 1X dilution buffer), and your library dilutions. Mix by pipetting 5x, minimizing bubbles.

Suggested plate map in figure 1.

- [ ] Briefly centrifuge plate and transfer to qPCR instrument
- [ ] Run qPCR as indicated in **Table 3**.

### Data Interpretation
- [ ] Export data to CSV
- [ ] Open Quantification Summary.csv
- [ ] Extract SQ (starting quantity) for each sample
- [ ] Multiple by dilution factor for  pM concentration of library
- [ ] Multiply by (399/average library size) to obtain final pM concentration of library

## QC

## Figures

![fig1](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/images/384-Well-Plate-Template-NEBNext.jpg)
**Figure 1**. Suggested plate map for 384 well

![fig2](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/images/std%20curve%20qPCR.jpg)
**Figure 2**. Expected Results. Note efficiency greater than 90%. At least 1 dilution of library should land between standards.

![fig3](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/images/melt%20curve%20qPCR.jpg)
**Figure 3**. Melt curve 

## Tables


**Table 1. qPCR Cycling Parameters**
Cycle                   |    	Temperature (˚C)     | Time
------------------------|----------------------------|------
Initial Denaturation    |	95	                     | 1 min
35 cycles\*:
Denature                | 95˚C                       | 15 sec
Extend                  | 63˚C                       | 45 sec
Melt in increments of 5s from 65˚C to 95˚C
Holding	                | 4˚C	Hold                 | 0 sec


