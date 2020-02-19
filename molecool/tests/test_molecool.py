"""
Unit and regression test for the molecool package.
"""

# Import package, test suite, and other packages as needed
import molecool
import pytest
import sys

def test_molecool_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "molecool" in sys.modules

def test_molecular_mass(methane_molcule):
    symbols, coordinates, molecular_mass = methane_molcule

    calculated_mass = molecool.calculate_molecular_mass(symbols)

    actual_mass = molecular_mass

    assert actual_mass == calculated_mass