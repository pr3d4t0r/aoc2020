# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from util import mainStart


# +++ constants +++

INITIAL_SEARCH_TOKEN = 'shiny gold bag'
TOKEN_DELIMITER = 'contain'


# *** functions ***

def loadExerciseDataFrom(fileName: str) -> list:
    data = [ b.strip() for b in open(fileName, 'r').readlines() if b != '\n' ]

    return data


def __extractFrom(text):
   ptr = text.index(TOKEN_DELIMITER)-2

   token = text[:ptr]

   return token



def searchBagPolicy(searchToken, data, validContainers):
    for datum in data:
        if searchToken in datum and searchToken != datum[:len(searchToken)]:
            validContainers.append(datum)

    return validContainers
    

def resolvePuzzle01Using(data):
    validContainers = list()
    searchToken     = INITIAL_SEARCH_TOKEN

    while searchToken:
        intermediateResults = searchBagPolicy(searchToken, data)

        if intermediateResults:
            validContainers.extend(intermediateResults)
        else:
            searchToken = None

        for result in intermediateResults:
            searchToken = __extractFrom(result)

    return -1


def resolvePuzzle02Using(data):
    return -1



def main(fileName:str = None):
    fileName = mainStart(fileName, 6)

    data = loadExerciseDataFrom(fileName)

    answer1 = resolvePuzzle01Using(data)
    answer2 = resolvePuzzle02Using(data)

    print('answer 1: %d' % answer1)
    print('answer 2: %d' % answer2)

    return answer1, answer2


# --- main ---

if '__main__' == __name__:
    main()

