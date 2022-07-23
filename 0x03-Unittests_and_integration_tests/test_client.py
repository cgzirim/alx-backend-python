#!/usr/bin/env python3
"""Defines unittest for client.GithubOrgClient class."""
import unittest
from fixtures import TEST_PAYLOAD
from unittest.mock import patch
from unittest.mock import PropertyMock
from client import GithubOrgClient
from parameterized import parameterized
from parameterized import parameterized_class


class TestGithubOrgClient(unittest.TestCase):
    """Unittest of for the class GithubOrgClient."""

    @parameterized.expand(["google", "abc"])
    @patch("client.get_json")
    def test_org(self, org, mock):
        """Test that GithubOrgClient.org returns the correct value."""
        obj = GithubOrgClient(org)
        obj.org
        url = "https://api.github.com/orgs/{}".format(org)
        mock.assert_called_once_with(url)

    @parameterized.expand([
        ("random-url", {"repos_url": "http://some_url.com"})
        ])
    def test_public_repos_url(self, name, result):
        """Test method returns correct output"""
        with patch("client.GithubOrgClient.org",
                   PropertyMock(return_value=result)):
            response = GithubOrgClient(name)._public_repos_url
            self.assertEqual(response, result.get("repos_url"))

    @patch("client.get_json")
    def test_public_repos(self, get_json_mock):
        """Test GithubOrgClient.public_repos"""
        get_json_mock.return_value = [
            {"name": "repo_0"},
            {"name": "repo_1"},
            {"name": "repo_2"},
        ]
        get_json_mock()
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock
        ) as mock:
            mock.return_value = [
                {"name": "repo_0"},
                {"name": "repo_1"},
                {"name": "repo_2"},
            ]
            obj = GithubOrgClient("abc")
            result = obj._public_repos_url
            self.assertEqual(result, mock.return_value)
            mock.assert_called_once()
            get_json_mock.assert_called_once()

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, repo, license_key, expected):
        """Tests GithubOrgClient.has_license."""
        method = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(method, expected)


@parameterized_class(
    ["org_payload", "repos_payload", "expected_repos", "apache2_repos"],
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Unittest of for the class GithubOrgClient's external requests."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up class before each method."""
        config = {
            "requests.get.return_value": TEST_PAYLOAD,
            "return_value.json.side_effect": [
                cls.org_payload,
                cls.repos_payload,
                cls.expected_repos,
                cls.apache2_repos,
            ],
        }
        cls.get_patcher = patch("requests.get", **config)
        cls.mock = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """Tear down class."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test for GithubOrgClient.public_repos."""
        obj = GithubOrgClient("Uber")
        self.assertEqual(obj.org, self.org_payload)
        self.assertEqual(obj.repos_payload, self.repos_payload)
        self.assertEqual(obj.public_repos(), self.expected_repos)
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """Test for GithubOrgClient.public_repos with arg"""
        obj = GithubOrgClient("Uber")
        assert True


if __name__ == "__main__":
    unittest.main()
