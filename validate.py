#!/usr/bin/env python3
# See: https://github.com/pr3d4t0r/aoc2020/blob/0001-AoC-day-2/LICENSE
# vim: set fileencoding=utf-8:


from util import day
from util import die

import sys


# *** functions ***

def main():
    if len(sys.argv) != 2:
        die('syntax:  validate passwors-file.ext', 1)

    day(2)


# --- main ---

if '__main__' == __name__:
    main()

