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


def isValidPassportNPC(passport):
    if all(field in passport.keys() for field in REQUIRED_PASSPORT_FIELDS):
        return True
    elif all(field in passport.keys() for field in REQUIRED_NPC_FIELDS):
        return True

    return False


def isValidStrict(passport):
    raise NotImplementedError
        

def countValidIn(passports, validator):
    count = 0
    for passport in passports:
        count += validator(passport)

    return count


def main(fileName = None):
    fileName = mainStart(fileName, 4)
    passports = loadPassportsFrom(fileName)

    validPassports = countValidIn(passports, isValidPassportNPC)

    print('valid passports or NPCs: %d' % validPassports)

    return validPassports


# --- main ---

if '__main__' == __name__:
    main()


