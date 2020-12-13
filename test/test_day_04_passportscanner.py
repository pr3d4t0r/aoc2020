# See: https://github.com/pr3d4t0r/aoc2020/blob/0001-AoC-day-2/LICENSE
# vim: set fileencoding=utf-8:

from aoc.day_04_passportscanner import _assertEyeColor
from aoc.day_04_passportscanner import _assertHairColor
from aoc.day_04_passportscanner import _assertHeight
from aoc.day_04_passportscanner import _assertPassportID
from aoc.day_04_passportscanner import _assertValidYearRangeFor
from aoc.day_04_passportscanner import _convertRawDataToDict
from aoc.day_04_passportscanner import countValidIn
from aoc.day_04_passportscanner import isValidPassport
from aoc.day_04_passportscanner import isValidPassportStrict
from aoc.day_04_passportscanner import loadPassportsFrom
from aoc.day_04_passportscanner import main

import pytest


# +++ constants +++

TEST_PASSPORTS_FILE_NAME = 'resources/test/passport-data-test.txt'
TEST_PASSPORTS_BAD_STRICT_FILE_NAME = 'resources/test/passport-bad-data-strict.txt'
TEST_PASSPORTS_GOOD_STRICT_FILE_NAME = 'resources/test/passport-good-data-strict.txt'


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

    assert isinstance(_passports, list)
    assert len(_passports) == 4
    assert _passports[0]['cid'] == '147'


def test_isValidPassport():
    assert isValidPassport(_passports[0])
    assert not isValidPassport(_passports[1])
    assert isValidPassport(_passports[2])
    assert not isValidPassport(_passports[3])


def test_countValidIn():
    assert 2 == countValidIn(_passports, isValidPassport)


def test__assertValidYearRangeFor():
    with pytest.raises(ValueError):
        _assertValidYearRangeFor('aaaa', 1920, 2002)

    with pytest.raises(AssertionError):
        _assertValidYearRangeFor('2009', 2010, 2030)

    with pytest.raises(AssertionError):
        _assertValidYearRangeFor('0', 2002, 2020)

    with pytest.raises(TypeError):
        _assertValidYearRangeFor(None, 1920, 2002)

    _assertValidYearRangeFor('1966', 1920, 2002)
        

def test__assertEyeColor():
    with pytest.raises(AssertionError):
        _assertEyeColor('red')

    _assertEyeColor('blu')


def test__assertPassportID():
    with pytest.raises(AssertionError):
        _assertPassportID('01234567')

    with pytest.raises(ValueError):
        _assertPassportID('12345678x')

    with pytest.raises(TypeError):
        _assertPassportID(None)

    _assertPassportID('012345678')


def test__assertHairColor():
    with pytest.raises(AssertionError):
        _assertHairColor('xxyyzz')

    with pytest.raises(AssertionError):
        _assertHairColor('#xxyyz')

    with pytest.raises(ValueError):
        _assertHairColor('#xxyyzz')

    _assertHairColor('#f0f0f0')


def test__assertHeight():
    with pytest.raises(AssertionError):
        _assertHeight('xxcmxx')

    with pytest.raises(ValueError):
        _assertHeight('xxcm')

    with pytest.raises(AssertionError):
        _assertHeight('149ft')

    with pytest.raises(AssertionError):
        _assertHeight('149cm')

    _assertHeight('181cm')
    _assertHeight('71in')


def test_isValidPassportStrict():
    assert isValidPassport(_passports[0])
    assert not isValidPassport(_passports[1])
    assert isValidPassport(_passports[2])
    assert not isValidPassport(_passports[3])


def test_countValidStrictIn():
    assert 2 == countValidIn(_passports, isValidPassportStrict)

    passports = loadPassportsFrom(TEST_PASSPORTS_BAD_STRICT_FILE_NAME)
    assert 0 == countValidIn(passports, isValidPassportStrict)

    passports = loadPassportsFrom(TEST_PASSPORTS_GOOD_STRICT_FILE_NAME)
    assert 4 == countValidIn(passports, isValidPassportStrict)


def test_main():
    assert main(TEST_PASSPORTS_FILE_NAME) == (2, 2,)
    assert main(TEST_PASSPORTS_GOOD_STRICT_FILE_NAME) == (4, 4,)
    assert main(TEST_PASSPORTS_BAD_STRICT_FILE_NAME) == (4, 0,)
 
