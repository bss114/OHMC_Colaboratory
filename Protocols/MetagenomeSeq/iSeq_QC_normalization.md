# iSeq QC and Normlization

## Background

There are many ways to normalize a sequencing library, but it can be difficult (and expensive) to perfectly normalize a pool. Because there are many variables (such as size) that can effect clustering efficiency, one of the best ways to normalize a sequencing library is to... sequence it. This can be accomplished using an iSeq 100 which utilizes the same chemistry and flow cell as the NovaSeq x, but at a significantly lower cost and read depth. Essentially, in this protocol, 1 µL of each library is combined in a tube, and run on the iSeq. The resulting read depths per sample are then used to adjust the pooling volumes for sequencing on a NovaSeq run. **Note: libraries that were prepared from at least 30ng of DNA should be relatively well normalized already and it is possible to directly proceed to this protocol. For samples that might have extreme differences in yield (this can be determined by looking at the tapestation QC), a pre-normalization to 1nM should be performed.

***

## Step 1: Prepare QC pool

### 1.1 Consumables
- [ ] Strip tubes (Ex. VWR 76468-978)
- [ ] 10 µL tips (1 tip per sample)
- [ ] Qubit assay tubes (Thermo Q32856)
- [ ] Qubit dsDNA HS assay kit (Thermo Q32854)
- [ ] Agilent Highsensitivity D1000 ScreenTape and sample buffer (Agilent 5067-5584 and 5067-5603)
- [ ] Illumina RSB
- [ ] PhiX (Illumina 15017666)

### 1.2 Procedure

- [ ] Using a strip tube and careful pipetting, transfer 1 µL from each sample library into a strip tube. **Alternatively: use the OT2 BlindPool.py script found in the OT2_scripts directory.**
- [ ] Combine the individual wells of the strip tube into a single microcentrifuge tube
- [ ] Measure concentration of pool using Qubit dsDNA kit
- [ ] Mix 2 µL tapestation sample buffer with 2 µL of pool
- [ ] Run sample on tapestation
- [ ] Integrate the region from 400 to 800 bp and record region molarity (pM)
- [ ] Cross reference the reported sample concentration from the Qubit against the sample concentration reported. If these values are not within 20% of eachother, proceed to use qPCR to measure library concentration. See protocol [here](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/Sequencing/LibraryQuant_NebNext.md).
- [ ] Dilute library to 1 nM in RSB
- [ ] Obtain a 1 nM aliquot of PhiX (**Note: Illumina supplies it at 10nM and diluted aliquots are stored in the lab freezer**)
- [ ] In a nuclease-free tube, combine 28.5 µL of the 1nM library with 1.5 µL of the 1 nM PhiX (5% spikein)
- [ ] Store at -20˚C or proceed


***

## Step 2: Sequence pool

### 2.1 Consumables
- [ ] Illumina iSeq 300 cycle kit (Cat # 20031371)
- [ ] RSB with Tween (comes with iSeq kit)
- [ ] 20 µL and 1000 µL tips

### 2.2 Procedure
- [ ] Thaw iSeq Cartridge the night before. Remove the cartidge from the box, but leave it in the tinfoil bag. Place the cartridge on the desk. At room temperature, cartridge needs to tbe thawed for between 9-18h. This corresponds to starting thawing at 5pm and starting the sequencing run before 11am the next day. See discussion [here](https://knowledge.illumina.com/instrumentation/iseq-100/instrumentation-iseq-100-reference_material-list/000002118).
- [ ] Bring flow cell out of fridge and leave at room temperature for at least 15 minutes
- [ ] To the 1nM library/PhiX mixture prepared in step 1.2, add 270 RSB/tween to dilute to the loading concentration of 100 pM
- [ ] Pipette 20 µL of the 100 pM library/phix into the appropriate well of the sequencing cartridge.
- [ ] Follow the instructions on the iSeq to start run
- [ ] When setting up the run, select the library prep kit as "Illumina DNA Prep", and the index adapter kit as "Illumina DNA-RNA UD Indexes Set A Tagmentation (v3)". Put any sample name under the first row of the sample sheet, and select well position "A1". **Note: the iSeq software makes uploading custom samplesheets somewhat of a pain, the proper sample sheet can be uploaded after the run is done; however, we need to make sure it captures 151x10x10x151 bases, and this will ensure it does.
- [ ] Monitor instrument for next 15 minutes as it does prerun checks. If any issues arise, immediately contact Illumina customer support.

*** 

## Step 3: Analyze data

- [ ] In [basespace](basespace.illumina.com/), find your run. Click the hourglass under the summary tab, and click requeue, then sample sheet. Under the data section, copy and past complete sample sheet that was exported from the "iSeq_samplesheet" tab of the MGS_RunTemplate.xlsx file.
- [ ] Hit requeue (analysis will take approximately 10 minutes depending on system load)
- [ ] On the indexing QC tab of the run, copy the Per Index results into the "iSeq_normalization" tab of the MGS_RunTemplate.xlsx file. *Note: someone needs to find a better way, but if you copy and paste into bbedit and use the find/replace funciton to first replace new lines `\r` with `\t`, then replace `\t([1-9][0-9]{0,3})\t` with `\r\1\t`
- [ ] Adjust the minimum pipette volume to ensure that most samples can be pooled within the available range of 0.5 to 20 µL
- [ ] Export the Loadings.csv file to proceed to final loading
- [ ] Remove any samples which are  not required

## Step 4: Repool samples
- [ ] On the Post PCR OT2, use the Pool Equimolar libraries from CSV program to pool samples uploading your loadings.csv file and following the instructions.
- [ ] Store final library at -20˚C until QC/sequencing.

## Step 5: Final QC

- [ ] Run library on High Sensitivity Tape Station to confirm final size distrobution and concentration (400-1000nt).
- [ ] Run on Qubit to get concentration
- [ ] Novogene requires ≥130 µL at 2-30nM (>2ng/µL) per NovaSeq X 25B lane. Actual loading concentration is 150 nM; however, this is after off-board NaOH denaturation (like MiSeq). Starting material per 25B flow cell denaturation protocol is 21 µL @ 2nM.
- [ ] If sample concentration is required, use Speedvac to dry sample to lower volume. If volume is brought up, bring up in RSB.
