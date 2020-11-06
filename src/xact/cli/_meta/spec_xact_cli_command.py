# -*- coding: utf-8 -*-
"""
Functional specification for the xact.cli.command module.

"""


import pytest


# =============================================================================
class Specify_envvar:
    """
    Spec for the xact.cli.command._envvar function.

    """

    # -------------------------------------------------------------------------
    def it_returns_a_string_prefixed_with_xact(self):
        """
        xact.cli.command._envvar returns a string prefixed with xact.

        """
        import xact.cli.command  # pylint: disable=C0415

        assert xact.cli.command._envvar('FOO') == 'XACT_FOO'


# -----------------------------------------------------------------------------
@pytest.fixture
def expected_help_text_main():
    """
    Return the expected help text for xact.cli.command.grp_main.

    """
    return (
        'Usage: main [OPTIONS] COMMAND [ARGS]...\n\n'
        '  Xact command line interface.\n\n'
        '  The xact command line interface provides the\n'
        '  user with the ability to start, stop, pause\n'
        '  and step an xact system.\n\n'
        '  An xact system is composed of one or more\n'
        '  process-hosts, each of which contains one or\n'
        '  more processes, each of which contains one or\n'
        '  more compute nodes.\n\n'
        'Options:\n'
        '  --help  Show this message and exit.\n\n'
        'Commands:\n'
    )


# =============================================================================
class SpecifyGrpMain:
    """
    Spec for the xact.cli.command.grp_main command group.

    """

    # -------------------------------------------------------------------------
    def it_displays_help_text_when_called_with_no_args(
                                                self, expected_help_text_main):
        """
        xact.cli.command.grp_main prints help text when called with no args.

        """
        import click.testing     # pylint: disable=C0415
        import xact.cli.command  # pylint: disable=C0415

        runner = click.testing.CliRunner()
        response = runner.invoke(xact.cli.command.grp_main)  # , ['--help'])
        response_text = ' '.join(line.strip() for line in
                                        response.output.splitlines())
        expected_text = ' '.join(line.strip() for line in
                                        expected_help_text_main.splitlines())

        assert response.exit_code == 0
        assert response_text.startswith(expected_text)

    # -------------------------------------------------------------------------
    def it_displays_help_text_when_called_with_help_arg(
                                                self, expected_help_text_main):
        """
        xact.cli.command.grp_main prints help text when called with a help arg.

        """
        import click.testing     # pylint: disable=C0415
        import xact.cli.command  # pylint: disable=C0415

        runner = click.testing.CliRunner()
        response = runner.invoke(xact.cli.command.grp_main, ['--help'])
        response_text = ' '.join(line.strip() for line in
                                        response.output.splitlines())
        expected_text = ' '.join(line.strip() for line in
                                        expected_help_text_main.splitlines())

        assert response.exit_code == 0
        assert response_text.startswith(expected_text)


# =============================================================================
class SpecifyErrorReporting:
    """
    Spec for error reporting when xact is invoked from the command line.

    """

    # -------------------------------------------------------------------------
    def it_displays_import_errors(self, skeleton_config):
        """
        xact.cli.command.grp_main prints error message on import error.

        """
        import xact.cli.command  # pylint: disable=C0415
        import xact.cli.util     # pylint: disable=C0415

        cfg = skeleton_config
        cfg_test_node_functionality = cfg['node']['test_node']['functionality']
        cfg_test_node_functionality['py_module'] = 'invalid.import.spec'

        xact.cli.util.run_test(cfg,
                               expected_exit_code = 1,
                               do_expect_stdout   = False,
                               do_expect_stderr   = True)
