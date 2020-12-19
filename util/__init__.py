# See: https://github.com/pr3d4t0r/aoc2020/blob/0001-AoC-day-2/LICENSE
# vim: set fileencoding=utf-8:


import fileinput
import sys


# +++ constants +++

RECORD_SEPARATOR = '\n\n'


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


def loadExerciseDataFrom(fileName: str, allowEmptyLines = False) -> list:
    if allowEmptyLines:
        data = [ line.strip() for line in fileinput.input(fileName) ]
    else:
        data = [ line.strip() for line in fileinput.input(fileName) if len(line) > 0 ]

    tokens = list()

    for line in data:
        tokens.extend(line.split())

    return data, tokens


def loadRawExerciseTextFrom(fileName: str) -> str:
    return open(fileName, 'r').read()


def loadExerciseDataAsTextRecordsFrom(fileName: str, recordSeparator = RECORD_SEPARATOR):
    rawData = loadRawExerciseTextFrom(fileName)

    return rawData.strip().split(RECORD_SEPARATOR)

