# imports
import os
import csv
import sys
import numpy as np
from rdkit import Chem
from rdkit.Chem import Descriptors, Crippen

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)
    smiles_list = [r[0] for r in reader]

# functions
def chemspider_equivalent_descriptors(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError(f"Invalid SMILES: {smiles}")
    logp = Crippen.MolLogP(mol)
    hbd = Descriptors.NumHDonors(mol)
    h_atoms = sum(a.GetTotalNumHs() for a in mol.GetAtoms())
    results = {
        "logp": logp,
        "hbd": hbd,
        "h_atoms": h_atoms,
    }
    print(smiles, results)
    return results

def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

def tmm_model(logp, hbd, h_atoms):
    logit = (
        -0.739
        + 0.671 * logp
        + 0.484 * hbd
        - 0.099 * h_atoms
    )
    return sigmoid(logit)


tmm = []
for smiles in smiles_list:
    desc = chemspider_equivalent_descriptors(smiles)
    proba = tmm_model(desc["logp"], desc["hbd"], desc["h_atoms"])
    tmm.append(proba)

input_len = len(smiles_list)
output_len = len(tmm)
if input_len != output_len:
    raise ValueError("Input and output lengths do not match.")

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["tmm_proba"])
    for t in tmm:
        writer.writerow([t])