# Bead Cleanup of Primary PCR Amplicons

## Theory

This protocol is to do a cleanup/size selection on PCR amplicons in which significant dimers have formed during primary PCR (i.e. >25 cycles of primary PCR). It is necessary to allow for accurate quantification after indexing to allow accurate pooling. Multiple types of beads can be used in this protocol, but it is suggested to either use AmpureXP beads or home-made beads at a ratio of 0.7x assuming a ~400nt amplicon. DNA is captured on to magnetic beads on the basis of a charge interaction which is mediated by PEG8000 in the bead buffer. The concentration of PEG determines the size range that will be bound, and the concentration can be shifted by changing the ratio of beads to product. Also, to facilitate high throughput cleanup, the PCR product is brought up in water to 20 µL. This protocol can also be used for people doing cleanup of full length 16S rRNA amplicons for sanger sequencing without bringing up the volume of the PCR product.

***

## Change log
- v0.1_July2025 JB: Initial testing and optimization
***

### 1.1 Equipment
- [ ] 125 µL Integra mini-96
- [ ] 96-well magnetic capture plate
- [ ] Plate centrifuge (Suggested USA Sci 2532-2000)

### 1.2 Consumables
- [ ] Magnetic capture beads (Ampure XP or home-made, see [here](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/Protocols/Misc/DIY_SPRIBeads.md) for recipe)
- [ ] 1.25 boxes of 125 µL Integra grip tips (Cat #6465)
- [ ] 80% Ethanol in a 1-well reservoir (made fresh daily)
- [ ] Nuclease free water in a 1-well reservoir
- [ ] 96 well plate (Suggested VWR 82006-704)


### 1.3 Protocol

#### Procedure
- [ ] Using a multichannel, preload 14 µL (0.7X) beads into each well of a 96-well plate corresponding to the samples to be cleaned up
- [ ] Using the program **PRIMARY CLEAN** on the 125 µL Integra:
  - [ ] Load tips
  - [ ] Transfer 11 µL from the water reservoir into the primary PCR plate (*Note: This step would be not be included for sanger amplicons*)
  - [ ] Mix well, and cover/briefly centrifuge if needed
  - [ ] Aspirate 20 µL from the Primary PCR plate into the 96-well plate containing beads
  - [ ] Mix well, and cover/briefly centrifuge if needed
  - [ ] Incubate for 5 minutes at room temp
  - [ ] Capture beads on magnet (~2 minutes)
  - [ ] Aspirate 33 µL from the tube and discard in waste
  - [ ] Wash 1:
    - [ ] Change Tips
    - [ ] Transfer 125 µL from the ethanol reservoir and transfer to cleanup plate. Do not mix.
    - [ ] Ensure beads are captured
    - [ ] Transfer 125 µL from the cleanup plate to the waste
  - [ ] Wash 2:
    - [ ] Change Tips
    - [ ] Transfer 125 µL from the ethanol reservoir and transfer to cleanup plate. Do not mix.
    - [ ] Ensure beads are captured
    - [ ] Transfer 125 µL from the cleanup plate to the waste being careful not to cross contaminate tips, or optionally, change tips again before proceeding
  - [ ] Cover/briefly centrifuge
  - [ ] Slowly remove any remaining ethanol from the plate
  - [ ] Air dry 2 minutes at room temperature
  - [ ] Change Tips
  - [ ] Aspirate 25 µL from the water plate and add to the dried beads off magnet
  - [ ] Pipette to mix
  - [ ] Incubate 2 minutes at room temperature
  - [ ] Cover/briefly centrifuge if needed
  - [ ] Capture beads on magnet (~ 2 minutes)
  - [ ] Transfer 20 µL of supernatant containing DNA to new plate for downstream analysis. For indexing, can directly use this product without further dilution.
