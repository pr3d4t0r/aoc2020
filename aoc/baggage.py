# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from util import mainStart

import re


# +++ constants +++

TARGET_BAG_TYPE = 'shiny gold'
TOKEN_DELIMITER = 'contain'


# *** functions ***

def loadExerciseDataFrom(fileName: str) -> list:
    data = [ b.strip() for b in open(fileName, 'r').readlines() if b != '\n' ]

    return data


def _defineRulesFrom(data) -> dict:
    regexBags = re.compile('([0-9]+) ([a-z ]+) bags?')

    rules = dict()
    for line in data:
        container = line[:line.find(' bags contain '):]
        rules[container] = dict()

        if 'contain no other bags' in line:
            continue

        for match in re.findall(regexBags, line):
            rules[container][match[1]] = int(match[0])

    return rules


def resolvePuzzle01Using(data):
    rules = _defineRulesFrom(data)
    shinyGoldBagContainers = [ TARGET_BAG_TYPE, ]
    maxContainers = -1

    while maxContainers != len(shinyGoldBagContainers):
        maxContainers = len(shinyGoldBagContainers)
        for rule in rules:
            for bagContainer in rules[rule]:
                if bagContainer in shinyGoldBagContainers and rule not in shinyGoldBagContainers:
                        shinyGoldBagContainers.append(rule)

    shinyGoldBagContainers.remove(TARGET_BAG_TYPE)

    return len(shinyGoldBagContainers), rules


def _resolveInnerBagsWith(rules, bagType):
    total:int = 0

    if not rules[bagType]:
        rules[bagType] = 0

    if isinstance(rules[bagType], dict):
        total = sum(((_resolveInnerBagsWith(rules, bagRule)+1)*rules[bagType][bagRule] for bagRule in rules[bagType]))
        rules[bagType] = total
    else:
        return rules[bagType]

    return total


def resolvePuzzle02Using(data):
    rules = _defineRulesFrom(data)
    return _resolveInnerBagsWith(rules, TARGET_BAG_TYPE)


def main(fileName:str = None):
    fileName = mainStart(fileName, 6)

    data = loadExerciseDataFrom(fileName)

    answer1, \
    rules = resolvePuzzle01Using(data)
    answer2 = resolvePuzzle02Using(data)

    print('answer 1: %d' % answer1)
    print('answer 2: %d' % answer2)

    return answer1, answer2


# --- main ---

if '__main__' == __name__:
    main()

