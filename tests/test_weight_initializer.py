#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_weight_initializer.py

Unit tests for the WeightInitializer class in weight_initializer.py.
"""

import unittest
import numpy as np
from src.layers.weight_initializer import WeightInitializer

class TestWeightInitializer(unittest.TestCase):
    
    def setUp(self):
        self.layers = 3
        self.num_wires = 4
        self.active_sd = 0.0001
        self.passive_sd = 0.1

    def test_init_weights_shape(self):
        """Test if the init_weights method returns weights of correct shape"""
        weights = WeightInitializer.init_weights(self.layers, self.num_wires, self.active_sd, self.passive_sd)
        expected_shape = (self.layers, (self.num_wires - 1) * 2 + self.num_wires + self.num_wires + (self.num_wires - 1) * 2 + self.num_wires + self.num_wires)
        self.assertEqual(weights.shape, expected_shape, f"Expected shape {expected_shape}, but got {weights.shape}")

    def test_init_weights_values(self):
        """Test if the init_weights method returns weights with appropriate values"""
        weights = WeightInitializer.init_weights(self.layers, self.num_wires, self.active_sd, self.passive_sd)

        # Extract different parts of the weights
        M = (self.num_wires - 1) * 2 + self.num_wires
        int1_weights = weights[:, :M]
        s_weights = weights[:, M:M + self.num_wires]
        int2_weights = weights[:, M + self.num_wires:M + self.num_wires + M]
        dr_weights = weights[:, M + self.num_wires + M:M + self.num_wires + M + self.num_wires]
        k_weights = weights[:, M + self.num_wires + M + self.num_wires:]

        # Check the standard deviations
        self.assertAlmostEqual(np.std(int1_weights), self.passive_sd, delta=0.01, msg="Interferometer 1 weights standard deviation out of bounds")
        self.assertAlmostEqual(np.std(s_weights), self.active_sd, delta=0.01, msg="Squeezing weights standard deviation out of bounds")
        self.assertAlmostEqual(np.std(int2_weights), self.passive_sd, delta=0.01, msg="Interferometer 2 weights standard deviation out of bounds")
        self.assertAlmostEqual(np.std(dr_weights), self.active_sd, delta=0.01, msg="Displacement weights standard deviation out of bounds")
        self.assertAlmostEqual(np.std(k_weights), self.active_sd, delta=0.01, msg="Kerr weights standard deviation out of bounds")

if __name__ == '__main__':
    unittest.main()

