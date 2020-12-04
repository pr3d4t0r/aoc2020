# See: https://github.com/pr3d4t0r/aoc2020/blob/0001-AoC-day-2/LICENSE
# vim: set fileencoding=utf-8:

from aoc.passportscanner import _convertRawDataToDict
from aoc.passportscanner import countValidIn
from aoc.passportscanner import isValidPassportNPC
from aoc.passportscanner import loadPassportsFrom
from aoc.passportscanner import main


# +++ constants +++

TEST_PASSPORTS_FILE_NAME = 'resources/test/passport-data-test.txt'


# +++ tests +++

_passports = None


def test__convertRawDataToDict():
    rawData = [ 'bogus:99', 'bs:32', ]
    passport = _convertRawDataToDict(rawData)

    assert isinstance(passport, dict)
    assert 'bogus' in passport
    assert passport['bogus'] == '99'
    assert len(passport) == 2


def test_loadPassportsFrom():
    global _passports

    _passports = loadPassportsFrom(TEST_PASSPORTS_FILE_NAME)

    x = _passports
    assert isinstance(_passports, list)
    assert len(_passports) == 4
    assert _passports[0]['cid'] == '147'


def test_isValidPassportNPC():
    assert isValidPassportNPC(_passports[0])
    assert not isValidPassportNPC(_passports[1])
    assert isValidPassportNPC(_passports[2])
    assert not isValidPassportNPC(_passports[3])


def test_countValidIn():
    assert 2 == countValidIn(_passports, isValidPassportNPC)


def test_main():
    x = main(TEST_PASSPORTS_FILE_NAME)


# test_loadPassportsFrom()
# test__convertRawDataToDict()
# test_isValidPassportNPC()
# test_countValidIn()

