#!/usr/bin/env python3
"""Defines test classes to test fuctions in ./utils."""
from ast import expr_context
import unittest
from unittest.mock import patch

from defer import return_value
from utils import get_json
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Unittest for the function utils.access_nested_map"""

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


class TestGetJson(unittest.TestCase):
    """Unittest for the fuction utils.get_json."""

    @parameterized.expand([
            ('http://example.com', {"payload": True}),
            ('http://holberton.io', {"payload": False})
        ])
    @patch("client.get_json")
    def test_get_json(self, url, expected, mock_get_json):
        """Tests that utils.get_json returns the expected result."""
        mock_get_json.return_value = expected
        self.assertEqual(mock_get_json(url), expected)
        # assert get_json(url) == expected
        mock_get_json.assert_called_once()
