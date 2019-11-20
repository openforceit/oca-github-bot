# Copyright (c) ACSONE SA/NV 2019
# Distributed under the MIT License (http://opensource.org/licenses/MIT).

import pytest

from orco_bot.commands import (
    InvalidCommandError,
    InvalidOptionsError,
    parse_commands,
)


def test_parse_command_not_a_command():
    with pytest.raises(InvalidCommandError):
        list(parse_commands("/orcobot not_a_command"))


def test_parse_command_multi():
    cmds = list(
        parse_commands(
            """
                ...
                /orcobot merge major
                /orcobot   merge   patch
                /orcobot merge patch
                /orcobot merge, please
                /orcobot merge  minor, please
                /orcobot merge minor, please
                /orcobot merge.
                /orcobot merge patch. blah
                /orcobot merge minor # ignored
                ...
            """
        )
    )
    assert [(cmd.name, cmd.options) for cmd in cmds] == [
        ("merge", ["major"]),
        ("merge", ["patch"]),
        ("merge", ["patch"]),
        ("merge", []),
        ("merge", ["minor"]),
        ("merge", ["minor"]),
        ("merge", []),
        ("merge", ["patch"]),
        ("merge", ["minor"]),
    ]


def test_parse_command_2():
    cmds = list(
        parse_commands(
            "Great contribution, thanks!\r\n\r\n"
            "/orcobot merge\r\n\r\n"
            "Please forward port it to 12.0."
        )
    )
    assert [(cmd.name, cmd.options) for cmd in cmds] == [("merge", [])]


def test_parse_command_merge():
    cmds = list(parse_commands("/orcobot merge major"))
    assert len(cmds) == 1
    assert cmds[0].name == "merge"
    assert cmds[0].bumpversion == "major"
    cmds = list(parse_commands("/orcobot merge minor"))
    assert len(cmds) == 1
    assert cmds[0].name == "merge"
    assert cmds[0].bumpversion == "minor"
    cmds = list(parse_commands("/orcobot merge patch"))
    assert len(cmds) == 1
    assert cmds[0].name == "merge"
    assert cmds[0].bumpversion == "patch"
    cmds = list(parse_commands("/orcobot merge"))
    assert len(cmds) == 1
    assert cmds[0].name == "merge"
    assert cmds[0].bumpversion is None
    with pytest.raises(InvalidOptionsError):
        list(parse_commands("/orcobot merge brol"))


def test_parse_command_comment():
    body = """
> {merge_command}
> Some comment {merge_command}
>> Double comment! {merge_command}
This is the one {merge_command} patch
    """.format(
        merge_command="/orcobot merge"
    )
    command = list(parse_commands(body))
    assert len(command) == 1
    command = command[0]
    assert command.name == "merge"
    assert command.bumpversion == "patch"
