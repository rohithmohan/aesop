# aesop-python
AESOP: Analysis of Electrostatic Structures of Proteins
Authors: Reed Harrison, Rohith Mohan, and Dimitrios Morikis

## Framework
- AESOP is a computational framework to explore electrostatic structures within proteins. The library depends on external tools including: APBS, PDB2PQR, Modeller, and ProDy
- **Atomic Selections**
	- All selection strings must be made according to the style of ProDy (http://prody.csb.pitt.edu/manual/reference/atomic/select.html)
- **Examples**
	- All materials for example cases are provided in the tests folder
- **Documentation**
	- HTML documentation provided within the docs folder 

## Methods
**Alascan**
	- Perform a computational alanine scan on a provided protein structure using a side-chain truncation scheme
	- Association free energies for mutatants (relative to the parent) may be predicted if 2 or more selection strings are provided
	- Users may restrict mutations to some region of the protein structure

**DirectedMutagenesis**
	- Perform a directed mutagenesis scan on a provided protein structure using Modeller to swap amino acids
	- Association free energies for mutatants (relative to the parent) may be predicted if 2 or more selection strings are provided
	- Mutations must be specified

**ElecSimilarity**
	- Compare electrostatic potential vector fields between multiple protein structures
	- If structures are very dissimilar, the user should superpose coordinates for each protein structure according to their desired method

## General Utilities
- aesop.plotScan()
	- Show bargraph summary of results from computational mutagenesis methods (Alascan, DirectedMutagenesis)
- aesop.plotESD()
 	- Show heatmap summary of results from methods exploring electrostatic similarity (ElecSimilarity)
- aesop.plotDend
 	- Show dendrogram summary of results from methods exploring electrostatic similarity (ElecSimilarity)
