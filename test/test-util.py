# See: https://github.com/pr3d4t0r/aoc2020/blob/0001-AoC-day-2/LICENSE
# vim: set fileencoding=utf-8:


from util import day
from util import die



# +++ tests +++

def test_day():
    today = day(0)
    assert isinstance(today, int)


def test_die():
    die('bogus', 0, unitTest = True)
    pass

