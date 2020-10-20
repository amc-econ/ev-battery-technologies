#!/usr/bin/env python

"""Tests for `ev_batteries_technologies` package."""


import unittest
from click.testing import CliRunner

from ev_batteries_technologies import ev_batteries_technologies
from ev_batteries_technologies import cli


class TestEv_batteries_technologies(unittest.TestCase):
    """Tests for `ev_batteries_technologies` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'ev_batteries_technologies.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
