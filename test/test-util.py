# See: https://github.com/pr3d4t0r/aoc2020/blob/0001-AoC-day-2/LICENSE
# vim: set fileencoding=utf-8:


from util import die
from util import mainStart



# +++ tests +++

def test_die():
    die('bogus', 0, unitTest = True)
    pass


def test_mainStart():
    assert mainStart('bogus-name.txt', 1) == 'bogus-name.txt'

