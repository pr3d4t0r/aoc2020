# See: https://github.com/pr3d4t0r/aoc2020/blob/0001-AoC-day-2/LICENSE
# vim: set fileencoding=utf-8:


from aoc.validate import extractPasswordsFrom
from aoc.validate import main
from aoc.validate import meetsOldPolicy
from aoc.validate import meetsPolicy


# +++ constants +++

TEST_VALIDATE_INPUT_FILE = './resources/test/passwords-test.txt'


# +++ tests +++

_passwords = None  # reused


def test_extractPasswordsFrom():
    global _passwords

    _passwords = extractPasswordsFrom(TEST_VALIDATE_INPUT_FILE)

    assert len(_passwords) == 4
    assert _passwords[0][1] == 'a'
    assert _passwords[2][0] == '2-9'


def test_meetsOldPolicy():
    assert meetsOldPolicy(_passwords[0])
    assert not meetsOldPolicy(_passwords[1])
    assert meetsOldPolicy(_passwords[2])


def test_meetsPolicy():
    assert meetsPolicy(_passwords[0])
    assert not meetsPolicy(_passwords[1])
    assert not meetsPolicy(_passwords[2])
    assert meetsPolicy(_passwords[3])


def test_main():
    assert main(TEST_VALIDATE_INPUT_FILE) == (3, 2)

