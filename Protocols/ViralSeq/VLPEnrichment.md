# VLP Purification Protocol from Fecal Sample

**Objective:** Purify the VLPs (Virus-Like Particles) from human stool samples, extract the DNA from the VLPs, and prepare the DNA for NGS on an Illumina Platform. The main advantages offered by VLP purification are adequate sequencing coverage for *de novo* assembly of abundant and rare viruses, greater confidence in viral sequence assignment, and the ability to sequence active and non-active viruses. The overall workflow will follow these steps:
- Sample Suspension and Homogenization
- Ultracentrifugation of 4-layer CsCl gradient
- Visualization of Purified Phage
- Viral DNA Extraction
- Sequencing Library Preparation

The isopycnic centrifugation step relies on the differences between sedimentation coefficients (Svedburg Units) and the buoyant densities of biological macromolecules to purify VLPs. This protocol utilizes a discontinuous gradient profile as the selection method for purifying bacteriophages, as it is designed to stop certain macromolecules from proceeding beyond a certain step. The densities used in the gradient depend on the target viruses' physiochemical properties, particularly its buoyant density. This protocol incorporates a 1.5 g/mL step as bacteriophages are expected to sediment between 1.4 - 1.5 g/mL. Simultaneously, many eukaryotic viruses should be excluded from the 1.5 g/mL step, as many possess densities of 1.3 g/mL or less.  

> [!IMPORTANT]
> It is important that steps 2 - 4 be completed in succession to minimize the loss of VLPs.

## Materials and Equipment
 
- [ ] 0.22-µm syringe filter
- [ ] 1.0 mm diameter Zirconia Beads
- [ ] 10 mL syringe with luer-lock
- [ ] 100mg of feces per sample
- [ ] 18 - 20 gauge needles
- [ ] 2 mL Screw Cap Tubes (Nuclease Free)
- [ ] Analytical Balance
- [ ] Beckman Coulter 13.2 mL, Open-Top Thinwall Ultra-Clear Tube, 14 x 89mm
- [ ] Biological Safety Cabinet (BSC)
- [ ] Chloroform, ACS, 99.8+% (Alfa Aesar U30H738)
- [ ] CsCl (Fisher Scientific, cat. no. BP1595)
- [ ] DNase I (1 U/µL) (cat. no. EN0525)
- [ ] EDTA, 0.5 M sterile solution (VWR 22J1956085)
- [ ] Epifluorescence Microscope
- [ ] [Fiji](https://imagej.net/software/fiji/downloads) 
- [ ] Glass Microscope Cover Slip
- [ ] Glass Microscope Slides
- [ ] Phosphate-buffered saline (PBS, 1X), sterile-filtered
- [ ] [QIAamp MinElute Virus Spin Kit](https://www.qiagen.com/us/products/discovery-and-translational-research/dna-rna-purification/multianalyte-and-virus/qiaamp-minelute-virus-kits?catno=57704)
- [ ] Qubit dsDNA HS Assay Kit (Fisher Scientific cat. no. Q32851)
- [ ] [Qubit Fluorometer](https://www.thermofisher.com/us/en/home/industrial/spectroscopy-elemental-isotope-analysis/molecular-spectroscopy/fluorometers/qubit.html)
- [ ] NanoDrop One/Oneᶜ Microvolume UV-Vis Spectrophotometer
- [ ] Swinging bucket rotor (Beckman SW40 Ti)
- [ ] SYBR™ Gold Nucleic Acid Gel Stain (Fisher Scientific cat. no. S11494) 
- [ ] Tissue Lyzer III (cat. no. 9003240)
- [ ] TissueLyser Adapter Set (cat. no. 69982)
- [ ] Ultracentrifuge
- [ ] Whatman Anotop 10 mm Syringe Filter, 0.02 µm (cat. no. 6809-1002)
- [ ] xGen™ ssDNA & Low-Input DNA Library Preparation Kit (cat. no. 10009859)
- [ ] Zymo Research DNA/RNA Shield (cat. no. R1100-50)

## 1. CsCl Gradient Setup
Before initiating the protocol, you should create your CsCl gradients the day before ultracentrifugation, as waiting too long before use will result in the CsCl precipitating out of the solution.
- Calculate the volume of filtrate (1x PBS) needed by taking the number of samples you are processing by utilizing the following simple formula:
	- Volume of Filtrate Required = *n*(11 mL)
		- Where *n* = number of samples
		- 11 is the sum of the volume of CsCl gradients required for each sample (three 1 mL gradients) and the dilution suspension volume for the fecal sample (8 mL)
- Utilizing a 10 mm syringe with a 0.022 µm filter attached via luer-lock, filter-sterilize the 1x PBS to the desired quantity as necessary for the number of samples you will be processing.

> [!TIP] 
> Utilizing a 10 mL syringe will allow the sample to pass through the membrane filter with ease as compared to larger syringe sizes.

- You'll need to set up the following CsCl gradients with the filtrate obtained from previous steps. The amount of CsCl to add to each fraction is dependent upon the starting density of the solution (~1.008 g/mL). Each fractional amount of CsCl can be calculated with the following general formula:
$`(\rho_{2} \times V_{f}) - (\rho_{1} \times V_{f}) = \text{CsCl (g) to add}`$ 

	- 1.15 g/mL 
	- 1.3 g/mL 
	- 1.5 g/mL 
	- 1.7 g/mL 
- Fractions are best prepared in either 10 mL or 50 mL conical tubes, and it is important to add the CsCl fractionally for all of the CsCl to dissolve properly in the 1x PBS.
- The density of your prepared fractions will need to be verified before proceeding. Take multiple 100 µL aliquots of your samples and weigh them on a scale to obtain the density. Adjust the amount of CsCl or filtrate to add to the prepared fractions to achieve the final density.

## 2. Preprocessing
The purpose of sample disruption/homogenization is to break down large particles within the solution, reduce within-sample variability, and lyse cell membranes. Lysing is necessary for exposing the inter-cellular constituents to the reagents of our extraction protocol. The following disruption of samples is intended for use with the TissueLyzer Adapter Set 2 x 24 (allows the processing of 48 samples) and TissueLyzer III. Be sure to prepare the stool suspensions in a BSC. 
- Prior to beginning be sure to wipe down the Adapter Set with detergent, microbicide, or up to 96% ethanol.
- Utilizing the 2 mL screw cap microcentrifuge tubes:
	- *First:* add 0.1 mL of 1.0 mm diameter Zirconia Beads into microcentrifuge tubes
	- *Second:* suspend 150 mg of stool in 1.5 mL of Zymo Research DNA/RNA Shield (or 1x PBS)
- Place samples in the tube holder in the accompanying 2 x 24 Adapter Set.
- Secure microcentrifuge tubes with caps and mount in the 2 x 24 Adapter Set.
- Attach the TissueLyser Adapter Set to the TissueLyser III, and close the lid before initiation of any program.
- Homogenize for 5 mins at 25 Hz.
- Centrifuge samples at low speed (2500 x g) for 5-10 mins.
- Collect supernatants. Utilizing a 10 mL syringe with an attached 0.22-µm filter syringe, dispense an equal volume of filtrate into a new microcentrifuge (1.5 mL) tube for each sample.

## 3. Ultracentrifugation
Before the preparation of the CsCl in the ultracentrifuge tubes, place the SW40-Ti rotor and the accompanying attachments in a 4°C refrigerator and turn on the ultracentrifuge to let it come down to 4°C at least 30 mins before running. Additionally, when taxiing samples back and forth between the ultracentrifuge and bench, it may be best to utilize a push cart to reduce the chance of disturbing boundary layers and sedimentation post-centrifugation.
- Dilute the collected supernatant in 8 mL of the 1.15 g/mL fraction before loading it into the ultracentrifuge tubes.
- Prepare the ultracentrifuge tubes (Fisher Scientific, cat. no. NC9194790) by loading 1 mL of each gradient in the tube (1.3, 1.5, 1.7 g/mL). Initially pipette the heaviest (1.7 g/mL) layer into the tube, then take care to carefully pipette the remaining layers by tilting the tube and slowly adding in the lighter densities. This layering can be achieved through the use of a micropipette and slowly releasing the solution along the side of the tube. 
- **Demarcate the boundaries between the different CsCl gradients as this will be crucial for identifying the fraction of interest to isolate from the ultracentrifuge tube.**
- Load the filtrate/sample onto CsCl layers with the use of a serological pipette, taking care not to disturb density layers.
- Place the tubes in their respective ultracentrifuge housings, and balance each of the tubes with excess 0.02 µm-filtered 1x PBS until there is less than 1 mg difference between tubes.
- Utilizing the Swinging Bucket Rotor, load samples into a centrifuge and spin at 60,000 x g (18,400 RPM) for 2 hours (4°C) to separate viral particles.
- Collect 1.3 to 1.5 g/mL fraction. This will be done through the use of an 18-gauge needle placed on a 10 mL syringe. Place the syringe just below the 1.5 g/mL layer and pierce the tube in a screwing motion until the needle is halfway through the tube. Take care not to disturb the column. Slowly withdraw the plunger and collect the 1 mL of the 1.5 g/mL fraction. **Be sure to do this in a secondary containment device as the tube will begin leaking contents upon penetration and removal.**
- Transfer the collected virion layers into a sterile 2 mL screw cap tube. This is to be done slowly as the shear forces may disrupt the VLPs that were just extracted.
- Reserve some of the fraction for visualization. Incubate with 20% vol/vol chloroform to remove bacterial vesicles for 10 minutes.
- Centrifuge at 4,000 x g for 5 minutes. 
- Collect the aqueous phase for further processing. Please be cognizant of the fact that the aqueous phase may be the top or bottom partition of the phase-separated liquids due to the density of the CsCl fraction and chloroform having similiar densities. 

> [!NOTE]
> Lipid-enveloped phages are sensitive to chloroform treatment and subsequent DNA recovery and viral particles observed under fluorescent microscopy may be reduced. If there are significant drops in recovered DNA/phage particles, then skip chloroform treatment. 

- Incubate each sample with 2.0 U DNase I per mL of sample for 3 hours at 37°C to remove free DNA that may remain on VLPs.
- Quench the reaction with a final concentration of 20 mM EDTA.

## 4. Microscopy Visualization and VLPs Counts
This step is to determine the presence of VLPs in your sample, and then quantify the abundance in each sample through the use of fluorescence microscopy. SYBR Gold can be viewed in the FITC channel, being excited with blue light and fluorescing with green light. Its peak absorption is 495 nm and its peak emission is 540 nm. More information on its absorption and emission can be found [here](https://www.thermofisher.com/order/fluorescence-spectraviewer/?SID=srch-svtool&UID=11494dna#!/). The exact microscope setup is dependent upon the available equipment, but this protocol was developed for use on a Confocal Microscope. This will be a "live" imaging process as fixing the samples will not be done. Quantification will require the [Fiji image software suite](https://imagej.net/software/fiji/downloads).
- Prepare the SYBR Gold working solution by performing a 1000x dilution. I.e., placing 5 µL of SYBR Gold into 45 µL of an isotonic buffer (PBS or SM Buffer).
- Aliquot your samples into 10 µL preparations in a strip tube container.
- Place 3.33 µL of the SYBR Gold working solution into the sample aliquots to achieve a final concentration of 250x.
	- The fluorescent capability of this dye decreases appreciably over time and thus samples should be stained and imaged as soon as possible.
- Samples should be visualized at greater than 600x magnification with an oil immersion lens. Phages will appear as dim points next to larger and brighter microbial cells. View the following images for reference: [Image 1](https://ars.els-cdn.com/content/image/1-s2.0-S2666166722000508-gr1.jpg) & [Image 2](https://www.nature.com/articles/nprot.2009.10/figures/5)
- Mount your samples on the slide with 10 µL and place a coverslip over the sample, taking care to ensure no air bubble formation.
- Make necessary adjustments to the microscope to ensure adequate focus of the samples and avoidance of oversaturation of fluorescent signal.
- Take 5 random micrographs throughout the slide, ensuring that each location is captured in triplicate.
- Import images into Fiji (a.k.a. ImageJ) and perform the following for phage quantification:
	- Convert to Grayscale (Image > Type > 8-bit)
	- Adjust contrast to an appropriate level for clear boundary delineation of VLPs (Image > Adjust > Brightness/Contrast)
	- Apply a threshold for VLP identification against the background signal (Image > Adjust > Threshold). This step will also convert the image into a binary image, which is necessary for the Analyze Particles function.
	- Analyze Particles (Analyze > Analyze Particles). Set a size range to exclude noise and only include phage in the counting process. Select options: Display results, Summarize, and Show Outlines
- Utilizing the count data, calculate the total number of VLPs, taking into account the dilution factor of the stain and the area of the image:
	- $\text{Number VLPs per Sample (X)} = \frac{p}{a}(b)(f)$
	- p = averaged number of VLPs per sample
	- a = area of the image
	- b = area of the coverslip
	- f = dilution factor
	- $\text{VLP's per 100 mg of feces (Y)} = \frac{X}{c}(d)$
	- c = volume loaded onto slide
	- d = total volume of extracted VLPs for 100 mg of feces
    - $`\text{VLPs per Gram of Feces} = Y \times 10`$

> [!NOTE]
> You should expect between 10<sup>8</sup> and 10<sup>10</sup> VLPs/g for stool samples.

## 5. DNA Extraction 
Follow the QIAamp MinElute Virus Spin Kit Protocol [here](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/ViralSeq/QIAmpMinEluteViral.md). Assess the quality of extracted DNA utilizing the Qubit and Nanodrop. If interested in RNA viruses, then it would be more appropriate to utilize the Qubit RNA IQ Assay.  

**Qubit**
- Utilizing the Qubit dsDNA HS Assay Kit, set up two tubes (standard 1 and standard 2) and a single assay tube for each sample.
- Prepare a working solution of the Qubit reagent by performing a 1:200 dilution in the Qubit Buffer. 200 µL of working solution will be needed for each standard and sample.
- For the standards and samples, add 190 µL of working solution to 10 µL of the respective solution into an individual Qubit tube.
- Vortex for 2-3 seconds and incubate at room temperature for 2 minutes.
- Insert the tubes into the Qubit fluorometer and take readings and record quantities.

**Nanodrop**
Utilize the elution solution from the DNA extraction protocol as the blank for the spectrophotometer. The following wavelengths will be of interest for your samples: 260 nm (nucleic acid absorption), 280 (proteins), and 230 (chaotropic and organic solvents).
- Pipette 1 µL of the sample onto the Nanodrop pedestal.
- Close the arm.
- The pedestal moves to automatically adjust for an optimal path length.
- Collect absorbance readings and record.
- When the measurement is complete, wipe surfaces with a lint-free wipe before continuing to the next sample.

## 6. Library Preparation
Follow the manufacturer's instructions on the use of the [IDT xGen ssDNA Library Prep Kit](https://sfvideo.blob.core.windows.net/sitefinity/docs/default-source/protocol/xgen-ssdna-and-low-input-dna-library-prep-kit-protocol.pdf?sfvrsn=b3a7e007_24).

## Sources
1. Bikel, S., Gallardo-Becerra, L., Cornejo-Granados, F., & Ochoa-Leyva, A. (2022). Protocol for the isolation, sequencing, and analysis of the gut phageome from human fecal samples. STAR protocols, 3(1), 101170. https://doi.org/10.1016/j.xpro.2022.101170
2. Bonilla, N., Rojas, M. I., Netto Flores Cruz, G., Hung, S. H., Rohwer, F., & Barr, J. J. (2016). Phage on tap-a quick and efficient protocol for the preparation of bacteriophage laboratory stocks. PeerJ, 4, e2261. https://doi.org/10.7717/peerj.2261
3. Castro-Mejía, J.L., Muhammed, M.K., Kot, W. et al. Optimizing protocols for extraction of bacteriophages prior to metagenomic analyses of phage communities in the human gut. Microbiome 3, 64 (2015). https://doi.org/10.1186/s40168-015-0131-4
4. Li J, George Markowitz RH, Brooks AW, Mallott EK, Leigh BA, Olszewski T, Zare H, Bagheri M, Smith HM, Friese KA, Habibi I, Lawrence WM, Rost CL, Lédeczi Á, Eeds AM, Ferguson JF, Silver HJ, Bordenstein SR. Individuality and ethnicity eclipse a short-term dietary intervention in shaping microbiomes and viromes. PLoS Biol. 2022 Aug 23;20(8):e3001758. doi: 10.1371/journal.pbio.3001758. PMID: 35998206; PMCID: PMC9397868.
5. Thurber, R., Haynes, M., Breitbart, M. et al. Laboratory procedures to generate viral metagenomes. Nat Protoc 4, 470–483 (2009). https://doi.org/10.1038/nprot.2009.10
