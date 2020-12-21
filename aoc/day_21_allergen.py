# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:

# Read:  itertools, more-itertools https://martinheinz.dev/blog/16
#        ref: https://pymotw.com/3/itertools/index.html
#        ref: https://realpython.com/python-itertools/
#        API ref: https://docs.python.org/3/library/itertools.html
#        API ref: https://more-itertools.readthedocs.io/en/latest/index.html


from collections import namedtuple
from collections import defaultdict

from util import loadExerciseDataAsTextRecordsFrom
from util import loadExerciseDataFrom
from util import loadRawExerciseTextFrom
from util import mainStart


FoodItem = namedtuple('FoodItem', ['ingredients', 'allergens'])


# +++ constants +++


# *** functions ***

def _extractFoodItemFrom(rawText):
    ingredients = list()
    allergens = list()
    allergensList = False
    for substance in rawText.split():
        if '(contains' in substance:
            allergensList = True
            continue

        if allergensList:
            allergens.append(substance.replace(',', '').replace(')', ''))
        else:
            ingredients.append(substance)

    return FoodItem(ingredients = ingredients, allergens = allergens)


def _classifyByPotentialAllergen(foods):
    allergenics = defaultdict(list)

    for food in foods:
        for ingredient in food.ingredients:
            for allergen in food.allergens:
                allergenics[allergen].append(ingredient)

    return allergenics
        

def resolvePuzzle01Using(data, tokens, rawText, textRecords):
    foods = list()

    for line in rawText.split('\n'):
        foods.append(_extractFoodItemFrom(line))

    x = _classifyByPotentialAllergen(foods)

    return -1


def resolvePuzzle02Using(data, tokens, rawText, textRecords):
    return -1



def main(fileName:str = None):
    fileName = mainStart(fileName, 21)

    data, tokens = loadExerciseDataFrom(fileName)
    rawText = loadRawExerciseTextFrom(fileName)
    textRecords = loadExerciseDataAsTextRecordsFrom(fileName)

    # ------------------------------------------
    # Answer 1
    # ------------------------------------------
    answer1 = resolvePuzzle01Using(data, tokens, rawText, textRecords)
    answer2 = resolvePuzzle02Using(data, tokens, rawText, textRecords)

    print('answer 1: %d, answer 2: %d' % (answer1, answer2))

    return answer1, answer2


# --- main ---

if '__main__' == __name__:
    main()

