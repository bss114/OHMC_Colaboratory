# Amplicon Sequencing Protocol 1- Primary PCR

## Theory
This protocol and the subsequent indexing steps were originally derived from a “Systematic improvement of amplicon marker gene methods for increased accuracy in microbiome studies” [doi:10.1038/nbt.3601](https://www.nature.com/articles/nbt.3601). The methods have been heavily modified to optimize throughput and minimize cost while also adapting to our equipment and supplies.

## Materials

- [ ] 384 Plates for qPCR (Biorad #HSP3865 OR Armadillo PCR plate Fisher AB3384)


## Protocol
***Location:** PCR hood or separate room/area from other steps*
- [ ] Wipe pipettes and work areas with DNaseAway or similar, treat PCR area with UV light for ~15 minutes.
- [ ] Generate enough PCR master mix for the number of samples you will be preparing in reagent reservoir (see **Table 2**). Mix well with a 1000ul pipette and/or rocking reservoir.
- [ ] Using 10 ul multichannel, transfer 9 ul of master mix into each well of qPCR plate which will be loaded. Be sure to consider the [96-to-384 well layout](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Templates/96_to_384_Integra.xlsx).
- [ ] Thaw gDNA plate on ice and briefly centrifuge to prevent cross contamination. **This centrifugation is essential.**
- [ ] Load gDNA on to Mini-96 and transfer 1 ul to qPCR plate
- [ ] Cover 384 well plate with optically clear plate seals
- [ ] Briefly centrifuge qPCR plate and transfer to qPCR instrument
- [ ] Run qPCR as indicated in **Table 3**.

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


