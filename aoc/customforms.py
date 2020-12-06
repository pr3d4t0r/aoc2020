# See: https://github.com/pr3d4t0r/aoc2020/blob/0001-AoC-day-2/LICENSE
# vim: set fileencoding=utf-8:


from util import mainStart


a_OFFSET = 97


# +++ constants +++

def loadExerciseDataFrom(fileName) -> list:
    # return [f.replace('\n', '') for f in ( b for b in open(fileName, 'r').read().split('\n\n') if len(b) )]
    return [ b for b in open(fileName, 'r').read().split('\n\n') if len(b) ]


def confirmedMixedAnswers(groupsData:list):
    results = list()
    for data in groupsData:
        groupAnswers = 26*[0]
        for answer in data.replace('\n', ''):
            groupAnswers[ord(answer)-a_OFFSET] = 1

        results.append(groupAnswers)

    allCounts = sum([ sum(result) for result in results ])

    return allCounts


def confirmedGroupAnswers(groupsData:list):
    results = list()
    for data in groupsData:
        groupAnswers = 26*[0]
        for answer in data.replace('\n', ''):
            groupAnswers[ord(answer)-a_OFFSET] += 1

        headCount = len(data.strip().split('\n'))

        for ptr in range(len(groupAnswers)):
            groupAnswers[ptr] = 0 if groupAnswers[ptr] != headCount else 1

        results.append(groupAnswers)


    accurateCounts = sum([ sum(result) for result in results ])

    return accurateCounts


# *** functions ***

def main(fileName:str = None):
    fileName = mainStart(fileName, 5)

    groupsData = loadExerciseDataFrom(fileName)
    allCounts = confirmedMixedAnswers(groupsData)
    accurateCounts = confirmedGroupAnswers(groupsData)

    print('allCounts = %d' % allCounts)
    print('accurateCounts = %d' % accurateCounts)

    return allCounts, accurateCounts


# --- main ---

if '__main__' == __name__:
    main()

