# gDNA Extraction with PowerSoil 96 Pro QIAcube HT kit 

## Theory

To effectively characterize a microbial community requires even lysis of all of its members. Some organisms like *E. coli* break open if you look at them the wrong way. Others like *E. lenta* require considerably more effort. Gram-positive organisms in stationary phase growth can be >90% peptidoglycan (cell wall) by weight. To ensure even lysis, mechanical lysis is preferred using shaking with beads at a high occurrence.

This protocol uses the current iteration of the PowerSoil reagents (previously MoBio) with later steps of the extraction performed in an automated fashion using a QIACube HT. This will ensure even lysis of communities, and isolation of high purity DNA with little residual PCR inhibitors which will cause problems in down stream enzymatic reactions (like those needed for sequencing or qPCR).

As this is a high throughput approach, users must be careful to maximize plate layouts. If a user has a limited number of samples, it may make more sense to use individual column tubes rather than 96 well format. These can be arrayed into plates for downstream analysis. Samples must be processed in multiples of 8 and loaded top to bottom, left to right. A minimum of 24 samples can be run; however, this is not time efficient and would be better done by hand using the conventional PowerSoil Reagents (Cat No 12855). If doing partial plates, cover the unused wells on the silica membrane plate with a sealing film.

A template has been provided to track sample layouts in 96 well plates. Download [here](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Templates/IndexTrackingSheet.xlsx). Please utilize it to ensure smooth integration into later workflows. Print a copy and keep in your lab book as well as a copy in the Sequencing Run log book.


*Note: The current QIAGEN manual can be found [here](https://www.qiagen.com/us/Resources/ResourceDetail?id=4eaebc72-77e5-48fb-8e28-3f64bfb66130&lang=en)*

## Equipment
- [ ] QIAcube HT
- [ ] Tissuelyzer III or similar (MPBio FastPrep 96)
- [ ] Floor centrifuge capable of spinning deep-well plates at 4500 g
- [ ] Single/multichannel pipettes capable of 200-1000ul volumes

## Consumables

- [ ] DNeasy 96 PowerSoil Pro QIAcube HT kit (5x96 Cat No 47021) *Note: store CD2 in 4˚C fridge*
- [ ] QIAcube HT Plastic ware (5x96 Cat No 950067)
- [ ] PowerBead Pro Plates (sold 4x96 - Cat No 19311)**See note below*
- [ ] 100% Ethanol suitable for molecular biology
- [ ] Barrier tips for single/multichannel pipette tips (DNase/RNase free)

*Note:Some users may prefer to use individual tubes when particularly worried about trace cross contamination. This may be important for pathogen detection. See Qiagen PowerBead Pro Tubes (Cat No 19301) or MPBio lysing matrix E*

***

## Protocol

### Preparation
***Location:** Pre-PCR hood
- [ ] Wipe pipettes and work areas with DNaseAway or similar, treat area with UV light for ~15 minutes
- [ ] Make sure centrifuge is at room temperature
- [ ] Bring buffer CD2 out of fridge and up to room temperature
- [ ] Ensure that Buffer AW1 and AW2 have had ethanol added. If not, add appropriate volumes as indicated on bottle. Mark that ethanol has been added with the date and your name
- [ ] Make sure that there is no precipitate in CD3 (SDS). If there is, heat in water bath until dissolved.
- [ ] Power on the QIACube HT, open Prep Manager Software, and run a UV cycle: click top right "Instrument", on left select UV lamp, click start. This runs for 30 min.
- [ ] Assemble QiaCube HT as per Figure 1. Specific instructions below:
- [ ] Insert the channeling block holder into the left (waste) chamber of the vacuum chamber.
- [ ] Press firmly on the sides of the channeling block holder to seat it in the chamber, sealing
the O-ring on the spigot into the drain.
- [ ] Place the channeling block into the channeling block holder.
- [ ] Place the QIAamp 96 Plate in the transfer carriage. Load the carriage with the QIAamp
96 Plate into the left (waste) chamber of the vacuum chamber.
- [ ] Ensure that the carriage is positioned to the left inside the vacuum chamber. Place the
riser block EMTR in the right (elution) chamber of the vacuum chamber, with the pin of
the riser block EMTR in top-right position. Load EMTR (without lid) into elution chamber.

![fig1](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/images/qiacube_vacuum_powersoil.jpg)
**Figure 1:** Schematic of Qiacube vacuum chamber. Taken from Manual. 



### Sample Disruption

***Location:** If samples are BSL2, conduct all work in Biosafety Cabinet, if BSL1, conduct all work in PCR cabinet.
- [ ] Wipe pipettes and work areas with DNaseAway or similar, treat PCR area with UV light for ~15 minutes.
- [ ] Briefly spin bead plate, or tubes to bring beads to bottom. Remove sealing mat.
- [ ] To each well/tube, add 800 uL CD1
- [ ] To each well (following sample recorded layout), transfer sample (200 ul fluid, <200mg feces, <250mg soil)
- [ ] Ensure there is no liquid on the top of bead plate which could prevent seal
- [ ] Seal the plate/tube; if using plate, you must use the sealing mat provided. Push in each bubble to ensure intact seal.
- [ ] Transfer plate/tubes to Tissuelyzer III. Ensure to include reusable silicon mat between the aluminum holder and the sealing mat of the bead plate. The 96w plate sits in the thin alumnim plate; the seal lays inside the thicker aluminum plate and may need to be trimmed before placing on top to ensure proper fit. This is a critical step. *Note: unit must be balanced. Place weight matched deep well plate on other holder if doing a single plate.*
- [ ] Tighten ratchets (blue knobs) of Tissuelyzer until they will no longer move; silver peg is lock/unlock.
- [ ] Run for 5 minutes at 25 Hz.
- [ ] Flip plate to opposite orientation.
- [ ] Run again for 5 minutes at 25 Hz.
- [ ] Centrifuge the plate for 6 minuets at 4,500g in floor centrifuge.
- [ ] While the samples are spinning, add 250 ul CD2 to each well of a new S-Block (deep well plate)
- [ ] Remove plate from centrifuge, careful to not disrupt pellet. Avoiding beads, transfer 450ul supernatant to the CD2 plate and mix. Mixing can be accomplished with pipetting or a plate vortex (be careful not to overflow wells, bring speed up slowly to ensure mixing)
- [ ] Centrifuge for 6 minutes at 4,500g
- [ ] Transfer 400-450 ul of supernatant into a fresh S block, careful to avoid any bead carryover (this can be done on QIAcube but is not faster than doing by hand)

### Sample Purification
***Location:** The lysis/disruption process has rendered any infectious agents inactive. Care must now focus on preventing contamination. Perform all work in laminar flow PCR hoods. Prepare all reagents within hoods and transfer to QIAcube when ready.
- [ ] In Prep Manager Software, select *DNeasy 96 PowerSoil Pro experiment*
- [ ] Enter kit and sample type/information if desired
- [ ] Select pre-treatment = "manual"
- [ ] Select Protocol: *DNeasy 96 PowerSoil Pro Protocol*
- [ ] Select the option for a vacuum check. This may be required if there are ANY concerns about clogging columns. This is a nightmare if it occurs. The best way to avoid it is to ensure that no beads/solid material have been transfered during Disruption steps.
- [ ] Deselect option for using TopElute Fluid (unless this is desired by user)
- [ ] Check auto-generate sample IDs (we will not retain this information, but you could important your sample names if desired)
- [ ] In the "Plate Assignment" screen, select the columns you want to run.
- [ ] In the worktable setup screen, load all supplies in the correct volumes and specified locations; note any directional items especially the elution tubes; pour reagent reservoirs in the PCR hood and label each-if doing multiple runs in a day, these can be reused. Unseal your samples last in the PCR hood and place the block. Uncover tips and tubes.
- [ ] Double check the waste bottle volume; however, this should be emptied after every use
- [ ] Put S block plate with supernatants from *Sample Disruption* in the designated position.
- [ ] Double check that deck layout matches image in Figure 2
- [ ] Select start run
- [ ] When vacuum check alert comes up (it will show expected timing in the software), ensure that all supernatants have cleared their wells. If not, evasive maneuvers might be required and those samples may be lost.
- [ ] When run is complete, label collection plate with computer printed label. Label must include the project name, user name, plate X of Y, and the date. See Figure 3 for example.

![fig2](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/images/QiaCube%20deck.jpg)
**Figure 2:** Image of deck set up for PowerSoil.

![fig2]()
**Figure 3:** Example of properly labelled plate.

### Cleanup

- [ ] Follow instructions in software for cleaning instrument
- [ ] Cover any tip racks that have leftover tips. Label them with your name and date. Place in drawer under QIAcube.
- [ ] Remove and discard all residual reagents in DNA extraction waste collection.
- [ ] Discard tip disposal box
- [ ] Clean any metal surfaces with ethanol
- [ ] Clean any plastic surfaces with a quat disinfectant

## QC

DNA yield does not necessarily dictate performance in downstream applications. Users must also be aware that they may not be able to detect DNA in low-biomass samples. Cherry picking samples and measuring DNA concentration with Nanodrop/QuBit may be performed. If using Nanodrop (>50ng/ul), double check 260/230 ratio to ensure >1.4. A ratio less than 1.4 may indicate carryover of wash buffers which will cause problem in down stream reactions. If this is observed for high yield samples, they may be diluted 100x before downstream processes. If the samples are lower yield samples, they may be cleaned up using a magnetic capture protocol like AmpureXP beads.
