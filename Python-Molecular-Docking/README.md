# Molecular-Docking-via-Jupyter-NoteBook-Python-based

Install the following packages via conda.
Create an environment called "Docking"
```
conda create --name Docking python=3.8
conda activate Docking
conda install -c schrodinger pymol 
conda install -c conda-forge py3dmol 
pip install vina    
conda install -c conda-forge openbabel
pip install meeko
pip install rdkit
conda install -c conda-forge pdbfixer
conda install rdkit cython   
pip install git+https://github.com/chemosim-lab/ProLIF.git
jupyter notebook molecular_docking_panda 
```

Before intitialising please install ADFR_Suite and add it to your bashrc. file so that you can access prepare_receptor and prepare_ligand command.  https://ccsb.scripps.edu/adfr/downloads/ 

Happy Docking!

