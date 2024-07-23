# xGen IDT ssDNA & Low-Input DNA Library Prep

**Objective**: To prepare a viral metagenome or any other sample type that will utilize the xGen IDT ssDNA & Low-Input DNA Library Prep for short-read sequencing on an Illumina platform.

## Contents:
- [Intended Use](#intended-use)
- [Materials and Equipment](#materials-and-equipment)
    - [Reagent Handling](#reagent-handling)
    - [Fragmentation](#fragmentation)
    - [Optional Concentration Step](#optional-concentration-step)
- [Preparation of Master Mixes and Ethanol](#preparation-of-master-mixes-and-ethanol)
- [Thermocycler Programming](#thermocycler-programming)
- [Protocol](#protocol)
    - [Denaturation](#denaturation)
    - [Adaptase Reaction](#adaptase)
    - [Extension Reaction](#extension)
    - [Ligation Reaction](#ligation)
    - [Indexing PCR](#indexing-pcr)
- [Library QC](#library-qc)
- [Bioinformatic Considertations](#bioinformatic-considerations)

## Intended Use
Library preparation is the first step of next-gen sequencing and is platform-dependent. Essentially, it is the process of manipulating input DNA to impart the physical ability for the DNA to adhere to the flow cell and allow for the assignment of DNA in a sample-specific manner. In general, the process of preparing sequencing libraries can be broken down into three steps:
- **Fragmentation and end repair:** Illumina platforms are short-read sequencers and thus require DNA fragments of a small size to be sequenced. After fragmentation, single adenine bases are added via an A-tailing reaction. This step allows adapter sequences with single thymine overhangs to base pair with target DNA.
- **Adapter ligation:** Adapters are ligated with the target DNA to generate a single piece of DNA that is now ready for sequencing on the Illumina flow cell. In addition to the adapter sequences, barcodes are included to allow for multiplexed sequencing runs. This allows for multiple DNA libraries to be sequenced simultaneously, dramatically reducing the per-sample sequencing cost. 
- **PCR amplification (optional):** Library amplification may be done if it is in line with your experimental goals. Post-amplification cleanup is to be performed using magnetic beads or a spin column. 

The xGen IDT ssDNA & Low-Input DNA Library Prep Kit is suitable for the following sample types:
- Damaged DNA samples
- Samples with a mixture of ssDNA & dsDNA
- Low-input DNA
- Viromes, metagenomes, and phageomes targeting for ssDNA & dsDNA bacteriophages
- Ancient DNA Samples

The workflow of this procedure is as follows:
![](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Misc/images/xGen_Workflow.png)

- **Adaptase technology:** Simultaneous tailing and ligation of R2 Stubby Adapter to ssDNA and dsDNA templates.
- **Extension:** Generates the second strand complementary to the template fragments.
- **Ligation:** Adds R1 Stubby Adapter to the original strand.
- **Indexing PCR:** PCR incorporates sample indices and full-length adapters.

## Materials and Equipment
- [ ] 0.2 mL magnets for individual tubes and plates
- [ ] 100% ethanol (200 proof)
- [ ] 50 mL conical tubes
- [ ] 96-well PCR Plates
- [ ] Aerosol-resistant, low retention pipettes and tips, 2 - 1000 µL
- [ ] Agilent 4200 TapeStattion System
- [ ] Covaris ultrasonicator
- [ ] D1000 Ladder and Sample Buffer (Agilent 5067-5583)
- [ ] D1000 ScreenTape (Agilent 50675582)
- [ ] DNA LoBind Tubes, 1.5 mL
- [ ] Low EDTA TE
- [ ] Microcentrifuge
- [ ] NEBNext Library Quant Kit
- [ ] Nuclease-free Water
- [ ] Optical tube 8X strip (Agilent 401428) with cap (401425)
- [ ] PCR tubes, 0.2 mL
- [ ] Programmable thermal cycler
- [ ] qPCR Instrument
- [ ] Qubit Fluorometer
- [ ] Qubit™ dsDNA HS Assay Kit
- [ ] Serological Pipettes (5 - 25mL)
- [ ] SPRISelect® or AMPure® XP beads
- [ ] TapeStation loading tips (Agilent 5067*5599)
- [ ] Vortex
- [ ] xGen IDT ssDNA & Low-Input DNA Library Prep Kit
- [ ] xGen UDI Primer Pairs

>[!NOTE]
> Store the xGen ssDNA & Low-Input DNA Library Prep Kit reagents at -20°C, except for the xGen Low EDTA TE Buffer, which is stored at room temperature.

### Reagent Handling
- For non-enzymatic reagents, thaw on ice, then briefly vortex to mix.
- For enzymatic reagents, remove from -20°C and thaw on ice 10 mins before use. 
- When creating master mixes, always include an excess volume of 5%.
- **Be sure to perform pre-PCR and post-PCR processes in the appropriately labeled clean benches.**

This kit accepts DNA from **10 pg to 250 ng**. It is important to know the amount of starting material because the number of PCR cycles run during the Indexing step is dependent upon this number. If utilizing very-low quantity DNA, then utilize the number of PCR cycles supported for the lowest input amount.

### Fragmentation
This kit has been specifically designed to be processed with fragment sizes of 200bp or 350bp and has been specifically validated with mechanical shearing (sonication) methods. A Covaris sonicator is available at the [Genomics Research Incubator (GRI)](https://www.huck.psu.edu/about/collaborative-ventures/genomics-research-incubator/about-the-genomics-research-incubator) in 303 Wartick. Please get in touch with the center for instrumentation requests.

The size of the fragmented library impacts the bead volumes in the subsequent cleanup steps for the extension, ligation, and indexing processes. For this protocol, we will be utilizing **a fragment size of 350 bp.**

### Optional Concentration Step
If you don't have sufficient DNA quantity for the 3 µL starting volume, you will need to concentrate with Zymo Research DNA Clean & Concentrator™ or another method and elute in 3 μl of Low EDTA TE buffer.

## Preparation of Master Mixes and Ethanol
>[!IMPORTANT]
>Please add the reagents in the order that they are listed in the tables below. Once done with assembling master mixes, STORE ON ICE UNTIL USE.

1. ***Adaptase Reaction Mix***
</head>
<body>
    <table>
        <tr>
            <th>Assembly Order</th>
            <th>Reagents</th>
            <th>Volume per Sample</th>
        </tr>
        <tr>
            <td rowspan="7">Pre-assemble</td>
            <td>Low ETDA TE</td>
            <td>2.3μl</td>
        </tr>
        <tr>
            <td>Buffer G1</td>
            <td>0.8 μl</td>
        </tr>
        <tr>
            <td>Reagent G2</td>
            <td>0.8 μl</td>
        </tr>
        <tr>
            <td>Reagent G3</td>
            <td>0.5 μl</td>
        </tr>
        <tr>
            <td>Enzyme G4</td>
            <td>0.2 μl</td>
        </tr>
        <tr>
            <td>Enzyme G5</td>
            <td>0.2 μl</td>
        </tr>
        <tr>
            <td>Enzyme G6</td>
            <td>0.2 μl</td>
        </tr>
        <tr>
            <td colspan="2"><strong>Total Volume</strong></td>
            <td><strong>5 μl</strong></td>
        </tr>
    </table>
</body>
</html>

2. ***Extension Reaction Mix***
</head>
<body>
    <table>
        <tr>
            <th>Assembly Order</th>
            <th>Reagents</th>
            <th>Volume per Sample</th>
        </tr>
        <tr>
            <td rowspan="4">Pre-assemble</td>
            <td>Low ETDA TE</td>
            <td>3.7 μl</td>
        </tr>
        <tr>
            <td>Reagent Y1</td>
            <td>0.4 μl</td>
        </tr>
        <tr>
            <td>Reagent W2</td>
            <td>1.4 μl</td>
        </tr>
        <tr>
            <td>Buffer W3</td>
            <td>3.5 μl</td>
        </tr>
        <tr>
            <td rowspan="1">Add just before use</td>
            <td>Enzyme W4</td>
            <td>0.4 μl</td>
        </tr>
        <tr>
            <td colspan="2"><strong>Total Volume</strong></td>
            <td><strong>9.4 μl</strong></td>
        </tr>
    </table>
</body>
</html>

3. ***Ligation Reaction Mix***
</head>
<body>
    <table>
        <tr>
            <th>Assembly Order</th>
            <th>Reagents</th>
            <th>Volume per Sample</th>
        </tr>
        <tr>
            <td rowspan="3">Pre-assemble</td>
            <td>Low ETDA TE</td>
            <td>0.8 μl</td>
        </tr>
        <tr>
            <td>Buffer B1</td>
            <td>0.4 μl</td>
        </tr>
        <tr>
            <td>Reagent B2</td>
            <td>2 μl</td>
        </tr>
        <tr>
            <td rowspan="1">Add just before use</td>
            <td>Enzyme B3</td>
            <td>0.4 μl</td>
        </tr>
        <tr>
            <td colspan="2"><strong>Total Volume</strong></td>
            <td><strong>4 μl</strong></td>
        </tr>
    </table>
</body>
</html>

4. ***Indexing PCR Reaction Mix***
</head>
<body>
    <table>
        <tr>
            <th>Assembly Order</th>
            <th>Reagents</th>
            <th>Volume per Sample</th>
        </tr>
        <tr>
            <td rowspan="3">Pre-assemble</td>
            <td>Low ETDA TE</td>
            <td>2 μl</td>
        </tr>
        <tr>
            <td>Reagent W2</td>
            <td>0.8 μl</td>
        </tr>
        <tr>
            <td>Reagent W3</td>
            <td>2 μl</td>
        </tr>
        <tr>
            <td rowspan="1">Add just before use</td>
            <td>Enzyme W4</td>
            <td>0.2 μl</td>
        </tr>
        <tr>
            <td colspan="2"><strong>Total Volume</strong></td>
            <td><strong>5 μl</strong></td>
        </tr>
    </table>
</body>
</html>

5. ***Ethanol Preparation*** 
- Create an 80% (vol/vol) solution of 200-proof ethanol and nuclease-free water. **Approximately 2.0 mL of ethanol will be used per library.**
## Thermocycler Programming
> [!WARNING]
> Be sure to set the lid temeprature to 105°C for all thermocycler programs **EXCEPT for Ligation Reaction (OFF)**.

- ***Denaturation***

| Step | Temperature (°C) | Time |
| :--: | :---: | :--: |
| 1 | 95 | 2 min |

- ***Adaptase***

| Step | Temperature (°C) | Time |
| :--: | :---: | :--: |
| 1 | 37 | 15 min |
| 2 | 95 | 2 min |
| 3 | 4 | Hold |

- ***Extension***

| Step | Temperature (°C) | Time |
| :--: | :---: | :--: |
| 1 | 98 | 30 sec |
| 2 | 63 | 15 sec |
| 3 | 68 | 5 min |
| 4 | 4 | Hold |

- ***Ligation***

| Step | Temperature (°C) | Time |
| :--: | :---: | :--: |
| 1 | 25 | 15 min |
| 2 | 4 | Hold |

>[!NOTE]
> The lid temperature for this program will be set to `OFF`

- ***Indexing PCR***

</head>
<body>
    <table>
        <tr>
            <th>Step</th>
            <th>Cycles</th>
            <th>Temperature (°C)</th>
            <th>Time</th>
        </tr>
        <tr>
            <td>1</td>
            <td>1</td>
            <td>98</td>
            <td>30 sec</td>
        </tr>
        <tr>
            <td rowspan="3">2</td>
            <td rowspan="3">Based on sample input (see table below)</td>
            <td>98</td>
            <td>10 sec</td>
        </tr>
        <tr>
            <td>60</td>
            <td>30 sec</td>
        </tr>
        <tr>
            <td>68</td>
            <td>60 sec</td>
        </tr>
        <tr>
            <td>3</td>
            <td>1</td>
            <td>4</td>
            <td>Hold</td>
        </tr>
    </table>
</body>
</html>

| Input (ng) | PCR Cycles |
| :--: | :--: |
| 250 | 3-5 |
| 100 | 4-6 |
| 10 | 7-9 |
| 1 | 10-12 |
| 0.1 | 14-16 |
| 0.01 | 17-19 |

## Protocol
The starting point for this protocol is post-fragmentation and assumes that you have a sufficient starting amount of DNA for your library. The bead clean-up steps utilize a left-side size selection to remove small fragments and unused adapters. 

### Denaturation
1. Preheat the thermocycler to 95°C.
2. Transfer the fragmented DNA sample to a 0.2 mL PCR tube and adjust the volume of the sample to a final volume of 3 µL using the Low EDTA TE, if necessary.
3. Place the samples in the thermocycler and run the denaturation program, listed above.
4. Transfer libraries onto ice upon completion of the thermocycling program. Leave for 2 minutes and then proceed with the Adaptase step to preserve the maximum amount of ssDNA substrate.

### Adaptase
1. Make sure the Adaptase thermocycler program is on and that it has reached 37°C prior to loading the libraries.
2. Add 5 µL of the pre-assembled Adaptase Reaction Mix to each PCR tube containing a 3 µL DNA library and mix pipetting or by gentle vortexing until. Spin down.
3. Place libraries into the pre-heated thermocycler and run the Adaptase program. 

### Extension
1. While the Adaptase program runs, ensure that Enzyme W4 is out on ice and is ready to be aliquoted before use in the Extension Master Mix. Be sure to pulse-spin the Extension Master Mix after the addition of Enzyme W4, and briefly spin it down. Keep on ice.
2. Once the Adaptase program concludes. Remove samples from the thermocycler. Add 9.4 µL of the Extension Master Mix to each PCR tube. 
3. Mix by pipetting or pulse-spin. Spin down.
4. Preheat the thermocycler to 98°C. Place the samples in the thermocycler and run the Extension Reaction program.
5. Once done with the Extension Reaction, proceed to bead cleanup with SPRISelect or AMPure XP beads.
6. Add the appropriate bead volume to each well, depending on the input size and concentration of your DNA library. Mix by vortexing. Briefly centrifuge.
<table>
  <thead>
    <tr>
      <th>Input</th>
      <th>Number of cleanups</th>
      <th>Sample volume (µL)</th>
      <th>Bead volume (µL)</th>
      <th>Elution volume (µL)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>&ge;1 ng, 200 bp</td>
      <td>Single cleanup</td>
      <td>17.4</td>
      <td>20.88 (ratio: 1.2X)</td>
      <td>20</td>
    </tr>
    <tr>
      <td>&ge;1 ng, 350 bp</td>
      <td>Single cleanup</td>
      <td>17.4</td>
      <td>13.92 (ratio: 0.8X)</td>
      <td>20</td>
    </tr>
    <tr>
      <td rowspan="2">&lt;1 ng, 200 bp</td>
      <td>1st cleanup</td>
      <td>17.4</td>
      <td>20.88 (ratio: 1.2X)</td>
      <td>20</td>
    </tr>
    <tr>
      <td>2nd cleanup</td>
      <td>20</td>
      <td>24 (ratio: 1.2X)</td>
      <td>20</td>
    </tr>
    <tr>
      <td rowspan="2">&lt;1 ng, 350 bp</td>
      <td>1st cleanup</td>
      <td>17.4</td>
      <td>13.92 (ratio: 0.8X)</td>
      <td>20</td>
    </tr>
    <tr>
      <td>2nd cleanup</td>
      <td>20</td>
      <td>24 (ratio: 0.8X)</td>
      <td>20</td>
    </tr>
  </tbody>
</table>

7. Incubate the libraries at room temperature for 5 minutes off-magnet.
8. Place the samples on a magnetic rack until a pellet is formed and the solution clears (~ 2 minutes)
>[!TIP]
> If the solution is not clear after 2 minutes, keep the plate on the magnet until the solution clears.
9. Remove and discard the clear supernatant; take care not to remove any beads.
10. Place back on the magnet, add 200 µL of 80% ethanol, and incubate for 30 seconds. Remove and discard the supernatant.
11. Repeat the previous step for a second wash.
12. Use a P20 pipette tip to remove any residual ethanol.
13. Remove libraries from the magnet, and add 20 µL of nuclease-free water to elute. Vortex. Briefly centrifuge.
14. Incubate for 5 minutes to elute DNA off beads.
15. Place on magnet and wait for the liquid to clear completely for 1-2 minutes. Transfer libraries into a new 96 well plate or strip tubes.
16. Place in a speed vacuum and concentrate at the following specifications:
    - 37°C, 5 PSI, 10 - 20 minutes
17. Add 4 µL of low EDTA TE Buffer, vortex to redissolve pellet, and briefly spin down.
18. If necessary, perform secondary bead cleanup after step 12 with the following directions:
    - Remove libraries from the magnet, add specified Elution Volume of Low EDTA Te Buffer, and gently vortex to resuspend the pellet.
    - Incubate for 5 minutes at room temperature.
    - Place samples on the magnet and wait for the solution to clear completely (~1-2 minutes).
    - Transfer libraries into a new well/tube. Run previous steps 6-17.
>[!NOTE]
>Safe Stopping Point. Samples can be briefly stored at 4°C or at -20°C overnight. 

### Ligation
1. Ensure the Ligation Master Mix is prepared. Add Enzyme B3 just before use.
2. Pulse-vortex the Master Mix, then briefly centrifuge. Keep the Master Mix on ice.
3. Pre-heat the thermocycler to the starting temperature of the Ligation program that was mentioned above.
4. Add 4 µL of the Ligation Master Mix to each library. 
5. Place samples in the pre-heated thermal cycler and run the Ligation Program. 
6. Perform post-ligation bead clean-up upon completion of the thermal cycling program. Below are the bead and sample volumes to be used during clean-up.

| Input | Sample volume (µL) | Bead volume (µL) | Elution volume (µL) |
| :--: | :--: | :---:| :--: |
| All inputs, 200 bp | 8 | 8 (ratio: 1.0x) | 4 |
| All inputs, 350 bp | 8 | 6.4 (ratio: 0.8x) | 4 |

7. Add the specified bead volume of SPRISelect/AMPure Beads to each well. Mix by vortexing. Then briefly centrifuge.
8. Incubate the libraries at room temperature for 5 minutes off-magnet.
9. Place onto the magnetic rack until the pellet is formed and the solution is clear. Make sure that the solution is clear before proceeding.
10. Remove and discard the cleared supernatant, take care not to remove any beads.
11. While keeping the samples on the magnet, add 200 µL of 80% ethanol, and incubate for 30 seconds. Remove and discard the supernatant.
12. Briefly centrifuge the libraries before loading them back onto the magnet.
13. Using a P20 pipette tip, remove any residual ethanol.
14. Remove libraries from the magnet, and add 20 µL of nuclease-free water to elute. Vortex.
15. Incubate for 5 minutes at room temperature, off-magnet.
16. Place on the magnet, waiting for the solution to become clear before proceeding. Transfer libraries into new 96-well plates or strip tubes.
17. Place in a speed vacuum and concentrate with the following specifications:
    - 37°C, 5 PSI, 10 - 20 minutes
18. Add 4 µL of Low EDTA TE Buffer. Vortex to resuspend the pellet. Briefly centrifuge.
>[!NOTE]
>Safe Stopping Point. Samples can be briefly stored at 4°C or at -20°C overnight. 

### Indexing PCR
This part of the protocol utilizes the xGen UDI Primers Plate 1, 8 nt. It contains unique dual indices, with a barcode length of 8. Each well is intended for a single library for the introduction of a specific index pair.
1. Thaw the xGen Indexing Primers at room temperature before use, and keep them on ice during use.
2. After thawing, briefly vortex the plates to mix. Briefly, centrifuge afterward to ensure that all liquid has collected at the bottom before piercing the seal.
3. Preheat the thermal cycler to the starting temperature of the Indexing PCR program as described above.
4. Ensure that the Indexing PCR Master Mix is ready. Add Enzyme W4 just before use.
5. Pulse-vortex the Master Mix for 10 seconds, then briefly centrifuge.
6. With the UDI Primer Plates, pre-pierce the seal with a pipette tip, then directly pipette 1 µL of the primer pair mixture into the wells containing the DNA libraries.
7. Add 5 µL of the Indexing PCR Master Mix to each well. 
8. Mix by pipetting or by gentle vortexing. Briefly centrifuge.
9. Place libraries within the thermocycler and run the Indexing PCR program.
10. Perform post-indexing PCR clean-up according to the following volumes:

| Input (bp) | Sample volume (µL) | Bead volume (µL) | Elution volume (µL) |
| :--: | :--: | :--: | :--: |
| 200 | 10 | 8.0 (ratio: 0.8x) | 10 |
| 350 | 10 | 8.5 (ratio: 0.85x) | 10 |

11. Add the specified bead volume of SPRISelect/AMPure Beads to each well. Mix by vortexing. Then briefly centrifuge.
12. Incubate the libraries at room temperature for 5 minutes off-magnet.
13. Place onto the magnetic rack until the pellet is formed and the solution is clear. Make sure that the solution is clear before proceeding.
14. Remove and discard the cleared supernatant, take care not to remove any beads.
15. While keeping the samples on the magnet, add 200 µL of 80% ethanol, and incubate for 30 seconds. Remove and discard the supernatant.
16. Briefly centrifuge the libraries before loading them back onto the magnet.
17. Using a P20 pipette tip, remove any residual ethanol.
18. Remove libraries from the magnet, and add 20 µL of nuclease-free water to elute. Vortex.
19. Incubate for 5 minutes at room temperature, off-magnet.
20. Place on the magnet, waiting for the solution to clear before proceeding. Transfer libraries into new 96-well plates or strip tubes.

>[!NOTE]
>Safe Stopping Point. Samples can be briefly stored at 4°C or at -20°C overnight. 

## Library QC

Please refer to QC + Normalization (iSeq) Protocol [here](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/MetagenomeSeq/iSeq_QC_normalization.md).

## Bioinformatic Considerations
The use of the xGen Adaptase technology in this kit will result in the addition of a low-complexity dinucleotide tail (8 nt in length) to the 3' end. They are observed at the beginning of Read 2 and may be observed towards the end of Read 1. These sequences may need to be removed depending on your computational needs.


