# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from aoc.day_14_bitmask import _applyFloatingBit
# from aoc.day_14_bitmask import _writeValue
from aoc.day_14_bitmask import loadExerciseDataFrom
from aoc.day_14_bitmask import main
# from aoc.day_14_bitmask import resolvePuzzle01Using
from aoc.day_14_bitmask import resolvePuzzle02Using
from aoc.day_14_bitmask import _generateAllFloatingBitValues
from aoc.day_14_bitmask import _applyMask


# +++ constants +++

TEST_DAY_14_BITMASK_FILE_NAME = 'resources/test/day_14_bitmask-test-data-01.txt'


# +++ tests +++

_data, _tokens = loadExerciseDataFrom(TEST_DAY_14_BITMASK_FILE_NAME)


# def test__writeValue():
#     mem = None
#     mask = None
# 
#     assert _writeValue(mem, mask)
# 
#     mask = { 29: 1, 34: 0 }
# 
#     mem = (8, 11)
#     assert 73 == _writeValue(mem, mask)
# 
#     mem = (7, 101)
#     assert 101 == _writeValue(mem, mask)
# 
#     mem = (8, 0)
#     assert 64 == _writeValue(mem, mask)


# def test_resolvePuzzle01Using():
#     answer = resolvePuzzle01Using(_data, _tokens)
# 
#     assert answer == 165


TEST_DAY_14_BITMASK_FILE_NAME = 'resources/test/day_14_bitmask-test-data.txt'

def test__generateAllFloatingBitValues():
    mask = '011X01X'
    maskBits = [bit for bit in mask]
    test = ['0110010', '0110011', '0111010', '0111011', ] 
    allMasks = _generateAllFloatingBitValues(maskBits)

    assert all(mask in test for mask in allMasks)


def test__applyMask():
    testMem = (42, 100)
    rawMask = '000000000000000000000000000000X1001X'
    testValue = '{:036b}'.format(58)

    memResult = _applyMask(testMem, rawMask)

    assert testValue == memResult[0]


def test__applyFloatingBit():
    testMem = ('000000000000000000000000000000111010', 100)
    rawMask = '000000000000000000000000000000X1001X'
    testResult = { 26: 100, 27: 100, 58: 100, 59: 100, } 
    
    allAddresses = _applyFloatingBit(testMem, rawMask)

    assert all(address in testResult for address in allAddresses.keys())


def test_resolvePuzzle02Using():
    _data, _tokens = loadExerciseDataFrom(TEST_DAY_14_BITMASK_FILE_NAME)

    answer = resolvePuzzle02Using(_data, _tokens)

    assert answer == 208


def test_main():
    _, answer2 = main(TEST_DAY_14_BITMASK_FILE_NAME) 
    assert answer2 == 208

