# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from util import loadExerciseDataFrom
from util import mainStart


# +++ constants +++


# *** functions ***

def _writeValue(mem, mask):
    if not mem:
        return True
    if not mask:
        return True

    value   = mem[1]
    for bitPos, mask in mask.items():
        bitMask = 2**(35-bitPos)
        if mask:
            value |= bitMask
        else:
            value &= bitMask

    return value


def resolvePuzzle01Using(data, tokens):
    addressSpace = dict()
    for seq, item in enumerate(data):
        if 'mask' in item:
            rawMask = item.replace('mask = ', '')
            mask = dict()
            for p, s in enumerate(rawMask):
                if s == '1' or s == '0':
                    mask[p] = int(s)
            continue

        mem = [int(x) for x in item.replace('mem[','').replace('] =', '').split()]
        addressSpace[mem[0]] = _writeValue(mem, mask)

    total = sum(addressSpace.values())

    return total


def _generateAllFloatingBitValues(rawMask):
    masks = [rawMask]
    for pos, bit in enumerate(rawMask):
        if bit != 'X':
            for mask in masks:
                mask[pos] = bit
            continue

        newMasks = list()
        for mask in masks:
            for bitValue in ('0', '1'):
                mask[pos] = bitValue
                newMasks.append(mask[:])
        masks = newMasks

    return [''.join(mask) for mask in masks]


def _applyMask(mem, rawMask):
    memResult = None
    rawAddress = mem[0]

    mask = int(''.join([bit if bit != 'X' else '0' for bit in rawMask]), 2)

    memResult = '{:036b}'.format(rawAddress|mask)

    return memResult, mem[1]


def _applyFloatingBit(mem, rawMask):
    allAddresses = dict()
    address = mem[0]
    value = mem[1]

    floatingBitAddress = [ bit for bit in address ]
    for pos, bit in enumerate(rawMask):
        if rawMask[pos] == 'X':
            floatingBitAddress[pos] = 'X'

    for sAddress in _generateAllFloatingBitValues([bit for bit in floatingBitAddress]):
        address = int(sAddress, 2)
        allAddresses[address] = value

    return allAddresses


def resolvePuzzle02Using(data, tokens):
    addressSpace = dict()
    for seq, item in enumerate(data):
        if 'mask' in item:
            mask = item.replace('mask = ', '')
            continue

        mem = [int(x) for x in item.replace('mem[','').replace('] =', '').split()]
        mem = _applyMask(mem, mask) # first converted address

        for address, value in _applyFloatingBit(mem, mask).items():
            addressSpace[address] = value

    total = sum(addressSpace.values())

    return total


def main(fileName:str = None):
    fileName = mainStart(fileName, 14)

    data, tokens = loadExerciseDataFrom(fileName)

    answer1 = resolvePuzzle01Using(data, tokens)
    answer2 = resolvePuzzle02Using(data, tokens)

    print('answer 1: %d' % answer1)
    print('answer 2: %d' % answer2)

    return answer1, answer2


# --- main ---

if '__main__' == __name__:
    main()

