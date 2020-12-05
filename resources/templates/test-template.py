# See: https://github.com/pr3d4t0r/aoc2020/blob/0001-AoC-day-2/LICENSE
# vim: set fileencoding=utf-8:


from aoc.%t% import main

import pytest


# +++ constants +++

TEST_%T%_FILE_NAME = 'resources/test/%t%-test-data.txt'


# +++ tests +++


def test_main():
    assert main(TEST_%T%_FILE_NAME) == (False, False)

