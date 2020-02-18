"""
Unit and regression test for the measure module.
"""

# Import package, test suite, and other packages as needed
import molecool
import pytest
import sys
import numpy as np


def test_calculate_distance():
    """Test that calculate_distance function calculates what we expect.
    And check that it returns an error if not a numpy array."""

    r1 = np.array([0, 0, 0])
    r2 = np.array([0, 1, 0])

    expected_distance = 1

    calculated_distance = molecool.calculate_distance(r1, r2)

    assert expected_distance == calculated_distance

    ## Now check for correct error raising.
    r1 = [0, 0, 0]
    r2 = [0, 1, 0]
    with pytest.raises(TypeError):
        molecool.calculate_distance(r1, r2)

def test_calculate_angle():
    """Test that calculate_angle function calculates what we expect."""
    r1 = np.array([0, 0, -1])
    r2 = np.array([0, 0, 0])
    r3 = np.array([1, 0, 0])

    expected_angle = 90
    calculated_angle = molecool.calculate_angle(r1, r2, r3, degrees = True)

    assert expected_angle == calculated_angle