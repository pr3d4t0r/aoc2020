# See: https://github.com/pr3d4t0r/aoc2020/blob/0001-AoC-day-2/LICENSE
# vim: set fileencoding=utf-8:


from collections import Counter
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


def meetsOldPolicy(passwordDef):
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

    password = Counter(sorted([letter for letter in passwordDef[2]]))
    
    return password[policy.letter] >= policy.min and password[policy.letter] <= policy.max


def main(fileName = None):
    if not fileName:
        if len(sys.argv) < 2:
            die('syntax:  validate passwords-file.ext', 1)
        else:
            fileName = sys.argv[1]

    day(2)
    
    valid = 0
    for password in extractPasswordsFrom(fileName):
        valid += 1 if meetsOldPolicy(password) else 0

    print('valid passwords (old) = %d' % valid)

    return valid


# --- main ---

if '__main__' == __name__:
    main()

