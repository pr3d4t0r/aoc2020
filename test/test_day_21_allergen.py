# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from aoc.day_21_allergen import main
from aoc.day_21_allergen import resolvePuzzle01Using
from aoc.day_21_allergen import resolvePuzzle02Using
from aoc.day_21_allergen import _extractFoodItemFrom
from aoc.day_21_allergen import _classifyByPotentialAllergen

from util import loadExerciseDataAsTextRecordsFrom
from util import loadExerciseDataFrom
from util import loadRawExerciseTextFrom


# +++ constants +++

TEST_DAY_21_ALLERGEN_FILE_NAME = 'resources/test/day_21_allergen-test-data.txt'


# +++ tests +++

_data, _tokens = loadExerciseDataFrom(TEST_DAY_21_ALLERGEN_FILE_NAME)

_rawText = loadRawExerciseTextFrom(TEST_DAY_21_ALLERGEN_FILE_NAME)

_textRecords = loadExerciseDataAsTextRecordsFrom(TEST_DAY_21_ALLERGEN_FILE_NAME)


def test__extractFoodItemFrom():
    foodItem = _extractFoodItemFrom('sqjhc fvjkl (contains soy')
    assert 'fvjkl' in foodItem.ingredients
    assert 'soy' in foodItem.allergens

    foodItem = _extractFoodItemFrom('mxmxvkd kfcds sqjhc nhms (contains dairy, fish)')
    assert 'mxmxvkd' in foodItem.ingredients
    assert 'fish' in foodItem.allergens

    foodItem = _extractFoodItemFrom('sqjhc mxmxvkd sbzzf')
    assert 'mxmxvkd' in foodItem.ingredients
    assert 'fish' not in foodItem.allergens
    assert not len(foodItem.allergens)


def test__classifyByPotentialAllergen():
    foods = list()
    for line in _rawText.split('\n'):
        foods.append(_extractFoodItemFrom(line))

    allergenics = _classifyByPotentialAllergen(foods)

    assert False


def test_resolvePuzzle01Using():
    answer = resolvePuzzle01Using(_data, _tokens, _rawText, _textRecords)

    assert answer == -1


def test_resolvePuzzle02Using():
    answer = resolvePuzzle02Using(_data, _tokens, _rawText, _textRecords)

    assert answer == -1


def test_main():
    assert main(TEST_DAY_21_ALLERGEN_FILE_NAME) == (-1, -1)


# TODO: --- remove before final check-in ---

# test__extractFoodItemFrom()
test__classifybyPotentialAllergen()
test_resolvePuzzle01Using()
# test_resolvePuzzle02Using()
# test_main()

