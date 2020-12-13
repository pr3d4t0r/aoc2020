# See: https://github.com/pr3d4t0r/aoc2020/blob/0001-AoC-day-2/LICENSE
# vim: set fileencoding=utf-8:


from util import mainStart


# +++ constants +++

REQUIRED_NPC_FIELDS = [ 'byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid', ]
REQUIRED_PASSPORT_FIELDS = REQUIRED_NPC_FIELDS.copy()
REQUIRED_PASSPORT_FIELDS.append('cid')


# *** functions ***

def _convertRawDataToDict(rawData):
    data = [ (datum.split(':')[0], datum.split(':')[1],) for datum in rawData ]

    return dict(data)


def loadPassportsFrom(fileName):
    passports = list()
    inputFile = open(fileName, 'r')
    rawPassportData = list()

    try:
        for line in inputFile:
            line = line.strip('\n')
            if len(line):
                rawPassportData.extend(line.split(' '))
            else:
                if rawPassportData:
                    passports.append(_convertRawDataToDict(rawPassportData))
                    rawPassportData = list()

    finally:
        try:
            inputFile.close()
        except:
            pass

    if len(rawPassportData):
        passports.append(_convertRawDataToDict(rawPassportData))

    return passports


def isValidPassport(passport):
    if all(field in passport.keys() for field in REQUIRED_PASSPORT_FIELDS):
        return True
    elif all(field in passport.keys() for field in REQUIRED_NPC_FIELDS):
        return True

    return False


def _assertValidYearRangeFor(yearString, start, stop):
    year = int(yearString)

    if year < start or year > stop:
        raise AssertionError()


def _assertEyeColor(eyeColor):
    if eyeColor not in ( 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth', ):
        raise AssertionError()


def _assertPassportID(passportID):
    if len(passportID) != 9:
        raise AssertionError()

    int(passportID)


def _assertHairColor(hairColor):
    if '#' not in hairColor or len(hairColor) != 7:
        raise AssertionError()

    int(hairColor.strip('#'), 16)


def _assertHeight(heightString):
    if len(heightString) < 4 or len(heightString) > 5:
        raise AssertionError()

    height = int(heightString[:-2])
    units = heightString[-2:]

    if units not in ('cm', 'in'):
        raise AssertionError()

    if units == 'cm':
        if height < 150 or height > 193:
            raise AssertionError()
    else:
        if height < 59 or height > 76:
            raise AssertionError()


def isValidPassportStrict(passport):
    if isValidPassport(passport):
        try:
            _assertValidYearRangeFor(passport['byr'], 1920, 2002)
            _assertValidYearRangeFor(passport['iyr'], 2010, 2020)
            _assertValidYearRangeFor(passport['eyr'], 2020, 2030)
            _assertEyeColor(passport['ecl'])
            _assertPassportID(passport['pid'])
            _assertHairColor(passport['hcl'])
            _assertHeight(passport['hgt'])
        except:
            return False
        else:
            return True
        
    return False


def countValidIn(passports, validator):
    count = 0
    for passport in passports:
        count += validator(passport)

    return count


def main(fileName = None):
    fileName = mainStart(fileName, 4)
    passports = loadPassportsFrom(fileName)

    validPassports = countValidIn(passports, isValidPassport)
    validPassportsStrict = countValidIn(passports, isValidPassportStrict)

    print('valid passports or NPCs: %d' % validPassports)
    print('valid passports (strict): %d' % validPassportsStrict)


    return validPassports, validPassportsStrict


# --- main ---

if '__main__' == __name__:
    main()

