# Protocol 3 - Equimolar pooling of amplicons

## Theory
Any given sequencing run produces a set number of reads: for example ~15 million from a MiSeq with v3 600 cycle reagents. In an ideal world, we would evenly distribute these reads among all samples. For example, if sequencing 150 samples, we should get 100,000 reads per sample. To get as close to this as possible, we need to pool equimolar amounts of each sample's individual sequencing library. While we have used manual pooling and Sequal plates in the past, manual pooling is prone to human error and is time consuming and Sequal plates have provided inconsistent results while leading to great enrichment of reads from negative controls that failed to provide evidence of amplification. This protocol will use the OT-2 to pool equal molar concentrations of each sample based on quantification using Pico-green dye which specifically quantifies dsDNA (allowing direct quantification of PCR amplicons). This is the same approach that the Qubit uses, but in a higher throughput format (Quant-iT). The dsDNA concentration of each product is used to **Note: all quantification and pooling should be done at the same time to avoid batch effects leading to poor normalization. Also, if significant primer dimer formation has occured, a bead cleanup is reccomended, see Optional Protocol 4: Ampure XP Wash.**

## Materials
- [ ] Quant-iT Picogreen dsDNA Assay Kit (Life Tech P7589)
- [ ] well black flat bottom NBS microplates (Corning 3650)
- [ ] Generic 50mL reservoirs (ex. VistaLab Reagent Reservoirs 50mL 2138127G)
- [ ] 200 µL multichannel pipette
- [ ] 10 ul multichannel pipette
- [ ] 1x 200ul filter tips (USA scientific 120-8710)
- [ ] 1x 10ul filter tips (USA scientific 1121-2710)
- [ ] Fluorescent plate reader (There is a Magellan that we can use in the Perdew lab)
- [ ] Nuclease free 1.5 mL microcentrifuge tube (eppendorf or alternative)
- [ ] Opentrons OT2
- [ ] Opentrons Gen2 20ul single channel
- [ ] 1 box 20ul opentrons filter tips

## Protocol
- [ ] For each 96 well plate, prepare 110 reactions (11mL dsDNA HS buffer, 55µL dsDNA HS reagent dye, scale appropriately) in a reagent reservoir.
- [ ] Fill each well of 96 well plate with 100 µL reaction mix (samples plate)
- [ ] Using an empty lane of a partial plate, or new plate if necessary, add 1 column with 100 µL each well for the standard curve.
- [ ] To full 96 well black plate (sample plate), transfer 1 µL of eached indexed PCR product and mix by pipetting
- [ ] Prepare a 2-fold dilution series using the 100 ng/µL lambda DNA standard provided with the quantit kit. Your standard curve should be 100, 50, 25, 12.5, 6.25, 3.125, 1.56 and 0 ng/µL.
- [ ] Transfer 1 µL of each standard to its designated column.
- [ ] Read on plate reader in Perdew lab, program Picogreen.
- [ ] Start by measuring flourescence on standard plate by setting the gain to automatic (Ex=480nm, Em=530nm).
- [ ] Copy the gain setting and flourescence values to the Picogreen tab of TrackingSheet.xlsx. **Note: You may consider just using 80 for the gain setting on the Perdew lab magellan**.
- [ ] Repeat measurement on full sample plate being sure to set gain to match the standard plate.
- [ ] Copy and paste results into Picogreen template as per **Figure 1**.
- [ ] Review the loading volumes and adjust ng amount if needed so that the volume being pipetted is >1ul; manually adjust volumes >10µL to be either 10µL or the average loading volume.
- [ ] Move to Loading.csv tab of index sheet, and click File > Save As > File Format: CSV UTF-8
- [ ] Remove lines which do not have a loading volume from the resulting csv file
- [ ] On the Post PCR OT2, use the Pool Equimolar libraries from CSV program to pool samples uploading your loadings.csv file and following the instructions.
- [ ] Prepare two lobind eppendorf tubes with labels and 20ul nuclease free water to ensure consistent delivery of volumes.
- [ ] Add one eppendorf tube in the A1 position of the tube rack, tucking the cap into the slot. Add a full box of 20ul tips to the deck.
- [ ] Calibrate all deck positions.
- [ ] Run protocol. **Estimated time of completion: 18 minutes/plate**
- [ ] Note, if the total volume to be pooled is over 1200ul, the protocol will pause and ask you to insert a fresh 1.5mL eppendorf tube.
- [ ] At completion of pooling, mix all pooled 1.5mL eppendorf tubes together (if pooling >1200ul)
- [ ] Prepare 1.2% agarose gel while OT2 is pooling.


## Figures
![](https://github.com/jbisanz/AmpliconSeq/raw/master/images/picogreen.png)

**Figure 1.** PicoGreen Normalization Tab.

![](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/images/amplicon_pooling.png?raw=true)

**Figure 2.** OT-2 deck layout. **Position 1-6:** Indexed PCR products. *Note: you may use any combination of plates 1-6 however ensure that their deck positions matches the loading.csv file.* **Position 7:** Eppendorf tube in position A1 of tube rack. **Position 8:** 20ul filter tips. Left Pipette is loaded with p20 single channel.
