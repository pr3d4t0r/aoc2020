# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from util import loadExerciseDataFrom
from util import mainStart


# *** functions ***

def resolvePuzzle01Using(earliestDeparture, busSchedule):
    departures = dict()

    for busID in busSchedule:
        start = earliestDeparture-(earliestDeparture%busID)
        nextDeparture = start+busID
        departures[nextDeparture] = busID

    upcomingDepartures = sorted([departure for departure in departures if departure >= earliestDeparture])

    departureWait = upcomingDepartures[0]-earliestDeparture
    nextBusID = departureWait*departures[upcomingDepartures[0]]

    return nextBusID, departureWait


def resolvePuzzle02Using(busSchedule):
    # Resolved via CRT after hint.
    # https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html

    earliestDeparture = 0
    runningProduct = 1

    for t, busID in enumerate(busSchedule):
        if busID == -1:
            continue

        while (t+earliestDeparture)%busID != 0:
            earliestDeparture += runningProduct

        runningProduct *= busID

    return earliestDeparture


def main(fileName:str = None):
    fileName = mainStart(fileName, 13)

    data, tokens = loadExerciseDataFrom(fileName)

    earliestDeparture = int(data[0])
    busSchedule = [int(busID) for busID in data[1].split(',') if busID != 'x']

    answer1, _ = resolvePuzzle01Using(earliestDeparture, busSchedule)

    busSchedule = [int(busID) if busID != 'x' else -1 for busID in data[1].split(',')]
    answer2 = resolvePuzzle02Using(busSchedule)

    print('answer 1: %d' % answer1)
    print('answer 2: %d' % answer2)

    return answer1, answer2


# --- main ---

if '__main__' == __name__:
    main()

