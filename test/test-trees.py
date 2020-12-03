# See: https://github.com/pr3d4t0r/aoc2020/blob/0001-AoC-day-2/LICENSE
# vim: set fileencoding=utf-8:


from aoc.trees import main


# +++ constants +++

TEST_TREES_MAP_FILE_NAME = "resources/test/trees-map-test.txt"


# +++ tests +++

def test_main():
    assert not main(TEST_TREES_MAP_FILE_NAME)

