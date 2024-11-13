from Bio.PDB import PDBParser
import numpy as np

def calculate_protein_dimensions(pdb_file, padding=0.0):
    parser = PDBParser()
    structure = parser.get_structure('protein', pdb_file)

    # Extract all atom coordinates and convert them to a NumPy array
    atom_coords = np.array([atom.coord for atom in structure.get_atoms()])

    # Calculate min and max coordinates in each dimension
    min_coord = np.min(atom_coords, axis=0)
    max_coord = np.max(atom_coords, axis=0)

    # Calculate the center and size
    center = (min_coord + max_coord) / 2
    size = (max_coord - min_coord) + padding

    return center, size

pdb_file = 'protein.pdb'  # Replace with your PDB file
center, size = calculate_protein_dimensions(pdb_file, padding=0.0)

print(f"Center: {center}")
print(f"Size: {size}")
