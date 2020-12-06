# See: https://github.com/pr3d4t0r/aoc2020/blob/0001-AoC-day-2/LICENSE
# vim: set fileencoding=utf-8:


from typing import Optional

import sys


# *** functions ***

def die(message:str, exitCode:int, unitTest:bool = False):
    if not unitTest:
        print(message)
        sys.exit(exitCode)


def mainStart(fileName:str, dayAoC:int) -> str:
    if not fileName:
        if len(sys.argv) < 2:
            die('missing input file name argument', 99)
        else:
            fileName = sys.argv[1]

    print('*** AoC Day %d ***\n' % dayAoC)

    return fileName

