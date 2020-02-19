"""
molecule.py
A Python package for analyzing and visualizing xyz files. For MolSSI Workshop Python Package development workshop.

Handles the primary functions
"""

import os
import numpy as np
import matplotlib.pyplot as plt
from .atom_data import atom_weights
from mpl_toolkits.mplot3d import Axes3D
from .measure import calculate_distance
def build_bond_list(coordinates, max_bond=1.5, min_bond=0):
    
    # Find the bonds in a molecule (set of coordinates) based on distance criteria.
    bonds = {}
    num_atoms = len(coordinates)

    for atom1 in range(num_atoms):
        for atom2 in range(atom1, num_atoms):
            distance = calculate_distance(coordinates[atom1], coordinates[atom2])
            if distance > min_bond and distance < max_bond:
                bonds[(atom1, atom2)] = distance

    return bonds


def calculate_molecular_mass(symbols):
    """Calculate the mass of a molecule.

    Parameters
    ----------
    symbols : list
        A list of elements.

    Returns
    -------
    mass : float
        The mass of the molecule
    """

    molecule_mass = float()
    for symbol in symbols:
        molecule_mass += atom_weights[symbol]

    return molecule_mass

if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
