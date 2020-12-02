# See: https://github.com/pr3d4t0r/aoc2020/blob/0001-AoC-day-2/LICENSE
# vim: set fileencoding=utf-8:


import sys


# *** functions ***

def die(message, exitCode, unitTest = False):
    if not unitTest:
        print(message)
        sys.exit(exitCode)


def day(number):
    print('*** AoC Day %d ***\n' % number)

    return number

