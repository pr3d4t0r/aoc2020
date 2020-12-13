# See: https://github.com/pr3d4t0r/aoc2020/blob/0001-AoC-day-2/LICENSE
# vim: set fileencoding=utf-8:


from aoc.day_03_trees import calculateAllImpactsUsing
from aoc.day_03_trees import calculateImpactsFrom
from aoc.day_03_trees import loadMapFrom
from aoc.day_03_trees import main


# +++ constants +++

TEST_TREES_IMPACTS = 7
TEST_TREES_IMPACTS_MULTIPLE_TRAVERSALS = 336
TEST_TREES_MAP_FILE_NAME = "resources/test/trees-map-test.txt"
TEST_TREES_TRAVERSALS = [ (1, 1), (3, 1), (5, 1), (7, 1), (1, 2), ]


# +++ tests +++

_treesMap = None


def test_loadMapFrom():
    global _treesMap

    _treesMap = loadMapFrom(TEST_TREES_MAP_FILE_NAME)

    assert len(_treesMap) == 11


def test_calculateImpactsFrom():
    assert calculateImpactsFrom(_treesMap, 3, 1) == TEST_TREES_IMPACTS


def test_calculateAllImpactsUsing():
    singleTraversal = [ (3, 1), ]

    assert calculateAllImpactsUsing(_treesMap, singleTraversal) == TEST_TREES_IMPACTS
    assert calculateAllImpactsUsing(_treesMap, TEST_TREES_TRAVERSALS) == TEST_TREES_IMPACTS_MULTIPLE_TRAVERSALS
    


def test_main():
    assert main(TEST_TREES_MAP_FILE_NAME) == (TEST_TREES_IMPACTS, TEST_TREES_IMPACTS_MULTIPLE_TRAVERSALS)

