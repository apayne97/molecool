"""File to define basic units of code for testing"""

import molecool
import pytest
import numpy as np

@pytest.fixture
def methane_molcule():
    symbols = np.array(['C', 'H', 'H', 'H', 'H'])
    coordinates = np.array([[1, 1, 1], [2.4, 1, 1], [-0.4, 1, 1], [1, 1, 2.4], [1, 1, -0.4]])
    molecular_mass = molecool.atom_data.atom_weights['C'] + molecool.atom_data.atom_weights['H'] + \
                     molecool.atom_data.atom_weights['H'] + molecool.atom_data.atom_weights['H'] + molecool.atom_data.atom_weights['H']
    return symbols, coordinates, molecular_mass