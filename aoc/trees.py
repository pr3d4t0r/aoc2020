# See: https://github.com/pr3d4t0r/aoc2020/blob/0001-AoC-day-2/LICENSE
# vim: set fileencoding=utf-8:


from util import mainStart


# *** functions ***

def loadMapFrom(fileName):
    raise NotImplementedError


def main(fileName = None):
    fileName = mainStart(fileName, 3)


# --- main ---

if '__main__' == __name__:
    main()

