#!/usr/bin/env python3
"""Test Module for utils"""

import unittest
from parameterized import parameterized
from utils import (access_nested_map)


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class that inherits from unittest.TestCase"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that the mtd returns the expected result"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
