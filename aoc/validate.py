# See: https://github.com/pr3d4t0r/aoc2020/blob/0001-AoC-day-2/LICENSE
# vim: set fileencoding=utf-8:


from collections import namedtuple

from util import day
from util import die

import sys


# *** functions ***

def extractPasswordsFrom(fileName):
    """
    Returns an array of tuples.
    """
    passwords = [ tuple(entry.replace('\n', '').replace(':', '').split(' ')) for entry in open(fileName, 'r').readlines() if len(entry.strip()) > 0]

    return passwords


def meetsPolicy(passwordDef):
    """
    passwordDef fields:

    0 - tranch, password policy lo/hi letter frequency/string
    1 - letter frequency
    2 - password
    """
    
    letterPolicy = namedtuple('LetterPolicy', ['letter', 'min', 'max',])
    policy = letterPolicy( letter = passwordDef[1],
        min = int(passwordDef[0].split('-')[0]),
        max =int(passwordDef[0].split('-')[1]) ,
    )

    # TODO: Use a Counter object here:
    password = passwordDef[2]

    return False


def main():
    if len(sys.argv) != 2:
        die('syntax:  validate passwords-file.ext', 1)

    day(2)
    
    passwords = extractPasswordsFrom(sys.argv[1])


# --- main ---

if '__main__' == __name__:
    main()

