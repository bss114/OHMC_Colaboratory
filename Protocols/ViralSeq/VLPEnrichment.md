# VLP Purification Protocol from Human Stool

**Objective:** Purify the VLPs (Virus-Like Particles) from human stool samples, extract the DNA from the VLPs, and prepare the DNA for NGS on an Illumina Platform. The main advantages offered by VLP purification are adequate sequencing coverage for *de novo* assembly of abundant and rare viruses, greater confidence in viral sequence assignment, and the ability to sequence active and non-active viruses. The overall workflow will follow these steps:

- Sample Suspension and Homogenization
- Filtration
- Organic Solubilization and DNase Incubation

> [!IMPORTANT]
> It is important to minimize the time between purification and extraction to prevent the loss of VLPs.

## Materials and Equipment

- [ ] 1.0 mm diameter Zirconia Beads
- [ ] 10 mL syringe with luer-lock
- [ ] 2 mL Screw Cap Tubes (Nuclease Free)
- [ ] 1g of feces per sample
- [ ] Amicon Ultra - 2 mL (UFC205024)
- [ ] Biological Safety Cabinet (BSC)
- [ ] Chloroform, ACS, 99.8+% (Alfa Aesar U30H738)
- [ ] DNase I (1 U/µL) (cat. no. EN0525)
- [ ] EDTA, 0.5 M sterile solution (VWR 22J1956085)
- [ ] Millex 0.45 µm Filter Unit PVDF Membrane (SLHVR33RS)
- [ ] Tissue Lyzer III (cat. no. 9003240)
- [ ] TissueLyser Adapter Set (cat. no. 69982)
- [ ] Whatman Anotop 10 mm Syringe Filter, 0.02 µm (cat. no. 6809-1002)

## Procedure

- [ ] Before beginning, wipe down the Adapter Set with detergent, microbicide, or up to 96% ethanol.
- [ ] Utilizing the 2 mL screw cap microcentrifuge tubes:
	- [ ] *First:* add 0.1 mL of 1.0 mm diameter Zirconia Beads into microcentrifuge tubes
	- [ ] *Second:* suspend 500 mg of stool in 1.0 mL of SM-plus Buffer

> [!NOTE]
> Suspending 1g of human stool in a 2 mL screw cap microcentrifuge tube will result in an unrecoverable supernatant. Be sure to divide your sample between multiple aliquots; in this case, 500mg is used. 

- [ ] Place samples in the tube holder in the accompanying 2 x 24 Adapter Set.
- [ ] Secure microcentrifuge tubes with caps and mount in the 2 x 24 Adapter Set.
- [ ] Attach the TissueLyser Adapter Set to the TissueLyser III, and close the lid before initiation of any program.
- [ ] Homogenize for 5 mins at 25 Hz.
- [ ] Centrifuge samples at low speed (2500 x g) for 5-10 mins.
- [ ] Collect supernatant into a new tube. Pellet bacteria with centrifugation at 10,000 x g for 10 mins. 
- [ ] Collect supernatant. Be careful in doing so, being sure to avoid the viscous mucus layer as it will clog the filter and result in the loss of your sample.
- [ ] Utilizing a 10 mL syringe with an attached 0.45-µm filter syringe, dispense filtrate into a new microcentrifuge (1.5 mL) tube.
- [ ] Wash the filter with 500 µL of SM buffer.
- [ ] Repeat for each sample.

***Chloroform Solubilization*** 

> [!IMPORTANT]
> Lipid-enveloped phages are sensitive to chloroform treatment, and subsequent DNA recovery and viral particles observed under fluorescent microscopy may be reduced. If there are significant drops in recovered DNA/phage particles, then skip the chloroform treatment.

- Add 0.2 volumes of chloroform to the supernatant, vortex, and incubate in a shaking incubator at room temperature for 10 min.
- Centrifuge at 21,000 x g for 5 minutes.
- Collect aqueous phase for further processing.

> [!NOTE]
> Safe stopping point at 4 degrees Celsius.

***DNase Incubation***

- Incubate each sample with 10.0 U DNase I per mL of sample for 1 hour at 37°C to remove free DNA that may remain on VLPs.
- Quench the reaction with a final concentration of 20 mM EDTA.
- Heat inactivation at 75° C for 30 mins.
- Reserve an aliquot for enumeration by fluorescence microscopy.

> [!NOTE]
> Storage conditions depend on the immediacy of the planned downstream processing. Viromes can be stored in SM Buffer at 4 degrees Celsius for up to a month for inoculation purposes and maintain DNA integrity for up to 100 days for metagenomic applications. Otherwise, long-term storage conditions at -80 degrees Celsius should be employed.


## References
1. Bonilla, N., Rojas, M. I., Netto Flores Cruz, G., Hung, S. H., Rohwer, F., & Barr, J. J. (2016). Phage on tap-a quick and efficient protocol for the preparation of bacteriophage laboratory stocks. PeerJ, 4, e2261. https://doi.org/10.7717/peerj.2261
2. Carroll-Portillo A, Coffman CN, Varga MG, Alcock J, Singh SB, Lin HC. Standard Bacteriophage Purification Procedures Cause Loss in Numbers and Activity. Viruses. 2021 Feb 20;13(2):328. doi: 10.3390/v13020328. PMID: 33672780; PMCID: PMC7924620.
3. Castro-Mejía, J.L., Muhammed, M.K., Kot, W. et al. Optimizing protocols for extraction of bacteriophages prior to metagenomic analyses of phage communities in the human gut. Microbiome 3, 64 (2015). https://doi.org/10.1186/s40168-015-0131-4
4. Cordova, A., Deserno, M., Gelbart, W. M., & Ben-Shaul, A. (2003). Osmotic shock and the strength of viral capsids. Biophysical journal, 85(1), 70–74. https://doi.org/10.1016/S0006-3495(03)74455-5
5. Guéroult M, Picot D, Abi-Ghanem J, Hartmann B, Baaden M. How cations can assist DNase I in DNA binding and hydrolysis. PLoS Comput Biol. 2010 Nov 18;6(11):e1001000. doi: 10.1371/journal.pcbi.1001000. PMID: 21124947; PMCID: PMC2987838.
6. Kleiner, M., Hooper, L.V. & Duerkop, B.A. Evaluation of methods to purify virus-like particles for metagenomic sequencing of intestinal viromes. BMC Genomics 16, 7 (2015). https://doi.org/10.1186/s12864-014-1207-4
7. Shack, J., & Bynum, B. S. (1964). Interdependence of variables in the activation of deoxyribonuclease I. Journal of Biological Chemistry, 239(11), 3843–3848. https://doi.org/10.1016/s0021-9258(18)91214-7
8. Thurber, R., Haynes, M., Breitbart, M. et al. Laboratory procedures to generate viral metagenomes. Nat Protoc 4, 470–483 (2009). https://doi-org.ezaccess.libraries.psu.edu/10.1038/nprot.2009.10



