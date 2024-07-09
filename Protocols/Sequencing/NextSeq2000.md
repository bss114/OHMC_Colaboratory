# NextSeq2000 XLEAP-SBS Sequencing Protocol for Amplicon Libraries

## Theory
After pooling equimolar amounts of the amplicon libraries and performing necessary clean up steps, the library should be diluted to 650-1000pM with a 40% PhiX spike (to provide nucleotide diversity) and run on the Illumina sequencer. The total loading volume should be 20-30ul.

## Materials
- [ ] PhiX Control v3 (Illumina 15017666)
- [ ] NextSeq 1000/2000 XLEAP-SBS P1 600 cycle reagent kit (Illumina 20101841)
  - [ ] cartridge stored at -20C with arrow labels pointing up!
  - [ ] RSB with Tween and Flow Cell stored at 4C

## Protocol
***Location:** clean benchtop*
**Prepare the cartridge:**
- [ ] Wearing gloves, remove foil package containing the cartridge from the -20C, place the box on the benchtop with the cartridge on top allowing air to circulate all around it.
- [ ] Make sure the position of the cartridge is such that the label faces up. Thaw for 12 hours at room temperature, not exceeding 16 hours.
**Load the flow cell:**      
- [ ] Remove the flow cell from 4C, allowing it to come to room temperature for 15 minutes.
- [ ] Wearing gloves, open the cartridge bag by tearing from the top notch on either side and remove the cartridge from the bag.
- [ ] Slowly invert the cartridge 10 times to mix reagents.
- [ ] Place the cartridge on the benchtop. Lift the cartridge by the arms approximately 1.5–2.5 in above the flat surface as shown, and release onto the benchtop five times, see **Figure 1**. (This reduces air bubbles and stabilizes cartridge components.)
- [ ] Remove the flow cell from the foil packet, holding it by the gray tab with the label on the tab facing up. Push to insert the flow cell into the slot on the front of the cartridge. An audible click indicates that the flow cell is inserted properly, the gray tab protrudes from the cartridge, see **Figure 2**. 
- [ ] Pull back and remove the gray tab to expose the flow cell.
- [ ] Note: it is worth saving the foil packet from the flow cell in the event of a run failure. Illumina will ask for the information on this packet.
**Load the library:**
- [ ] Using a new pipette tip, pierce the Library reservoir and push the foil to the edges to enlarge the hole.
- [ ] Load the library to the bottom of the reservoir by slowly lowering the pipette tip to the bottom of reservoir and then pulling back just slightly before dispensing. Avoid touching the foil. See **Figure 3**.
- [ ] Following the prompts on the instrument screen, insert the cartridge (label facing up and flow cell towards the sequencer), upload your sample details (csv or BaseSpace), select your data output folder, and click sequence.
- [ ] Notes: Read length is 270, indexes are 10.
**Clean up:**
- [ ] When the run is complete, eject the cartridge from the sequencer and pour out the contents as chemical waste to be collected (the drainage plug is under the Illumina logo on the side). The cartridge can then be discarded.
- [ ] Power cycle the instrument.

## QC
You can monitor the run progress and estimated completion on the monitor or on your BaseSpace account.

## Figures
**Figure 1**. 
![Lift/tap the cartridge on a benchtop five times](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/images/CartridgeTapping.png)

**Figure 2**. 
![Insert the flow cell into the cartridge](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/images/InsertFlowCell.png)

**Figure 3**. 
![Load the library into the cartridge](https://github.com/BisanzLab/OHMC_Colaboratory/blob/main/images/LoadLibrary.png)

## References
[Illumina reference guides](https://support-docs.illumina.com/IN/NextSeq10002000/Content/IN/NextSeq2000_1000/Protocol_seq_xleap.htm)
[Additional resources](https://support-docs.illumina.com/IN/NextSeq10002000/Content/IN/FrontPages/NextSeq10002000.htm)
