# RNA Extraction using QiaCube HT

## Theory

Describe here

## Materials

- [ ] RNeasy 96 QIAcube HT kit (74171)
- [ ] QIAcube HT plasticware (950067)
- [ ] QIAzol (79306)
- [ ] RNase-free DNase (79254)
- [ ] PowerBead lysis tubes
- [ ] Ethanol
- [ ] Chloroform

## Considerations
Recommended starting material for Mammalian cells 5x10^5. Approximate yield 1.5-2 ug per 10^5 cells.
Recommended starting material for tissues is 40mg. For adipose tissue, up to 80mg. For thymus, spleen, or intesting only 20mg. If stored in RNAlater, use half of these amounts. More details are provided in the [handbook](https://www.qiagen.com/us/Resources/ResourceDetail?id=7fde26d6-5c5e-4ed7-a535-b25d3753580e&lang=en).
Ideally tissues should be flash-frozen or processed immediately.
Maximim binding capacity for each column is 100ug RNA.

## Preparation
- [ ] Wipe pipettes and work areas with RNaseAway or similar, treat area with UV light for ~15 minutes
- [ ] Power on the QIACube HT (back left switch), open Prep Manager Software, and run a UV cycle: click top right "Instrument", on left select "UV lamp", click start. This runs for 30 min
- [ ] ensure Ethanol has been added to Buffer RWT and Buffer RPE
- [ ] perform all steps at room temperature
- [ ] DO NOT use bleach at any step as it is not compatible with guanidine.

## Sample Disruption
*Location: If samples are BSL2, conduct all work in Biosafety Cabinet, if BSL1, conduct all work in PCR cabinet.
- [ ] weigh tissues and put in PowerBead tubes on dry ice as quickly as possible. Do not allow tissues to thaw.
- [ ] remove tubes from dry ice and immediately add 750ul QIAzol per sample.
- [ ] secure tubes in TissueLyserII and run for 5 min at 25Hz. 
- [ ] rotate the TissueLyser rack to all for even homogenization and repeat for another 5 min at 25Hz.
      
After disruption, samples can be stored in Buffer RLT or Qiazol at -80C.
The lysis/disruption process has rendered any infectious agents inactive. Care must now focus on preventing contamination. Perform all work in laminar flow PCR hoods. Prepare all reagents within hoods and transfer to QIAcube when ready.

## RNA Extraction
*Location: If samples are BSL2, conduct all work in Biosafety Cabinet, if BSL1, conduct all work in PCR cabinet.
- [ ] allow samples to sit at room temperature 5 min.
- [ ] centrifuge at 6000xg for 1 min.
- [ ] add 150ul chloroform to each sample. 
- [ ] cap securely and shake vigorously with inversion for 15 sec.
- [ ] allow samples to sit at room temperature for 3 min.
- [ ] centrifuge at 6000xg for 15 min at 4C.
- [ ] recover the aqueous (upper) phase into a fresh S-block; the volume should be approximately 350ul.
- [ ] proceed to loading on the QIAcube HT.

## Optional DNase treatment
- [ ] One 96-well plate requires two vials of RNase-free DNase. Dissolve each vial in 550ul of the RNase-free water provided.
- [ ] Mix by gentle inversion, do not vortex.
- [ ] For 96 samples, prepare 1090ul DNase plus 7.63mL Buffer RDD.
- [ ] Add this solution to a reagent trough and place on the indicated worktable position.

## QIAcube HT setup ![Figure 1](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/images/QIAcubeHT_RNeasy_assembly.png)
- [ ] Insert the channeling block holder into the left chamber of the vacuum chamber. Press firmly to seat it correctly and sealing the O-ring on the spigot into the drain.
- [ ] Place the channeling block into the holder.
- [ ] Place the RNeasy 96 column plate into the transfer carriage; load into the left chamber of the vacuum chamber.
- [ ] Place the riser block EMTR into the right (elution) chamber of the vacuum chamber with the pin of the riser block EMTR in the top right position.
- [ ] Load labeled EMTR elution muicrotubes rack into the elution chamber positioning A1 in the top left.
- [ ] In Prep Manager Software, select RNeasy 96 experiment and select sample type.
- [ ] Select pre-treatment = "manual"
- [ ] Select Protocol: RNeasy cell or tissue
- [ ] Select the option for a vacuum check. This may be required if there are ANY concerns about clogging columns. This is a nightmare if it occurs. The best way to avoid it is to ensure that no beads/solid material have been transfered during Disruption steps.
- [ ] Select the optional step for on-plate DNase digestion.
- [ ]  In advanced: Deselect option for using TopElute Fluid (unless this is desired by user), click Next.
- [ ]  Check auto-generate sample IDs (we will not retain this information, but you could important your sample names if desired), click Next.
- [ ]  In the "Plate Assignment" screen, select the columns you want to run. Samples must be in columns of 8.
- [ ]  In the worktable setup screen, load all supplies in the correct volumes and specified locations; note any directional items especially the labeled elution tubes; pour reagent reservoirs in the PCR hood and label each-if doing multiple runs in a day, these can be reused. Unseal your samples last in the PCR hood and place the block. Uncover tips and tubes.
- [ ]  Double check the waste bottle volume; however, this should be emptied after every use in the satellite accumulation area next to the fume hood.
- [ ]  Put S block plate with supernatants from Sample Disruption in the designated position with A1 in the top left.
- [ ]  Double check that deck layout matches image in [Figure 2](link to image) and close the cover.
- [ ]  Select start run and save the run file.
- [ ]  When vacuum check alert comes up (it will show expected timing in the software), ensure that all supernatants have cleared their wells. If not, evasive maneuvers might be required and those samples may be lost.
- [ ]  Store extracted RNA at -80C.

## Cleanup
- [ ] Follow instructions in software for cleaning instrument.
- [ ] Remove components and rinse with dH2O, removing any residual salts. 
- [ ] Clean any metal surfaces with ethanol, allow to air dry.
- [ ] Wipe plastic surfaces with a quat disinfectant.
- [ ] Cover any tip racks that have leftover tips. Label them with your name and date. Place in drawer under QIAcube.
- [ ] Remove and discard all residual reagents in DNA extraction waste collection (satellite accumulation area).
- [ ] Discard tips in disposal box, S-block, and column plate as biohazard waste.
