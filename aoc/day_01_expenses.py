# See: https://github.com/pr3d4t0r/aoc2020/blob/0001-AoC-day-2/LICENSE
# vim: set fileencoding=utf-8:


from util import mainStart


# *** functions ***


def loadExpensesFrom(fileName):
    return sorted([int(entry) for entry in open(fileName, 'r').readlines()])


def find2020TwoEntriesProductIn(entries):
    for a in range(len(entries)):
        for b in range(a, len(entries)):
            if entries[a]+entries[b] == 2020:
                return entries[a]*entries[b]


def find2020ThreeEntriesProductIn(entries):
    for a in range(len(entries)):
        for b in range(a, len(entries)):
            for c in range(b, len(entries)):
                sumEntries = entries[c]+entries[a]+entries[b]
                if sumEntries == 2020:
                    return entries[a]*entries[b]*entries[c]


def main(fileName = None):
    fileName = mainStart(fileName, 1)

    expenses = loadExpensesFrom(fileName)
    magicProductTwo = find2020TwoEntriesProductIn(expenses)
    magicProductThree = find2020ThreeEntriesProductIn(expenses)

    print('magic product (two factors) = %d' % magicProductTwo)
    print('magic product (three factors) = %d' % magicProductThree)

    return magicProductTwo, magicProductThree


# --- main ---

if '__main__' == __name__:
    main()

