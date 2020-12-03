# See: https://github.com/pr3d4t0r/aoc2020/blob/0001-AoC-day-2/LICENSE
# vim: set fileencoding=utf-8:


from aoc.validate import extractPasswordsFrom
from aoc.validate import meetsPolicy


# +++ constants +++

TEST_VALIDATE_INPUT_FILE = './resources/test/passwords-test.txt'


# +++ tests +++

_passwords = None


def test_extractPasswordsFrom():
    global _passwords

    _passwords = extractPasswordsFrom(TEST_VALIDATE_INPUT_FILE)

    assert len(_passwords) == 3
    assert _passwords[0][1] == 'a'
    assert _passwords[2][0] == '2-9'


def test_meetsPolicy():
    meetsPolicy(_passwords[0])


test_extractPasswordsFrom()
test_meetsPolicy()

