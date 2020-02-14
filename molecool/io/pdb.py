"""
Functions for manipulating pdb files.
"""

import numpy as np


def open_pdb(file_location):
    """Read a pdb file

    The pdb file must specify the atom elements in the last column, and follow
    the conventions outlined in the PDB format specification.

    Paramters
    ---------
    file_location : str
        Path to the pdb file.

    Returns
    -------
    symbols : np.array
        Array of single character ATOM symbols
    coords : np.array
        Array of xyz float coordinates
    """
    with open(file_location) as f:
        data = f.readlines()

    coordinates = []
    symbols = []
    for line in data:
        if 'ATOM' in line[0:6] or 'HETATM' in line[0:6]:
            symbols.append(line[76:79].strip())
            atom_coords = [float(x) for x in line[30:55].split()]
            coordinates.append(atom_coords)

    coords = np.array(coordinates)
    symbols = np.array(symbols)

    return symbols, coords