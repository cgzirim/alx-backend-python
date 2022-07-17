#!/usr/bin/pyhton3
"""Defines a test class for util.access_nested_map."""
import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Test the function access_nested_map"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map function returns the expected result."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
            ({}, ("a",), "KeyError('a')"),
            ({"a": 1}, ("a", "b"), "KeyError('b')")
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test access_neste_map raises KeyError for none existing keys."""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(repr(e.exception), expected)
