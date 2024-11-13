from Bio.PDB import PDBParser, Selection
import numpy as np

def calculate_binding_site_center(pdb_file, residues):
    parser = PDBParser()
    structure = parser.get_structure('protein', pdb_file)
    model = structure[0]

    coords = []
    for chain_id, res_num in residues:
        try:
            chain = model[chain_id]
            # Access the residue
            residue = chain[res_num]
            # Get the Cα atom coordinate
            atom = residue['CA']
            coords.append(atom.coord)
        except KeyError:
            print(f"Warning: Residue {res_num} in chain {chain_id} not found in the PDB file.")
            continue

    if len(coords) == 0:
        raise ValueError("No valid residues found. Please check the residue IDs and chain IDs.")

    # Calculate the center of the binding site
    center = np.mean(coords, axis=0)
    return center, np.ptp(coords, axis=0)

pdb_file = 'protein.pdb'  # Replace with your PDB file
residues = [('A', 12), ('B', 20), ('B', 26)]  # Replace with your chain ID and residue numbers

try:
    center, size = calculate_binding_site_center(pdb_file, residues)
    print(f"Binding Site Center: {center}")
    print(f"Binding Site Size: {size}")
except ValueError as e:
    print(e)
