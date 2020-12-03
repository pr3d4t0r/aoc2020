# See: https://github.com/pr3d4t0r/aoc2020/blob/0001-AoC-day-2/LICENSE
# vim: set fileencoding=utf-8:


from aoc.expenses import find2020ThreeEntriesProductIn
from aoc.expenses import find2020TwoEntriesProductIn
from aoc.expenses import loadExpensesFrom
from aoc.expenses import main


# --- constants ---

TEST_EXPENSES_FILE_NAME = 'resources/test/expenses-test.txt'
TEST_MAGIC_PRODUCT_TWO = 514579
TEST_MAGIC_PRODUCT_THREE = 241861950


# +++ tests +++

_expenses = None


def test_loadExpensesFrom():
    global _expenses

    _expenses = loadExpensesFrom(TEST_EXPENSES_FILE_NAME)

    assert _expenses
    assert isinstance(_expenses, list)
    assert isinstance(_expenses[0], int)


def test_find2020TwoEntriesProductIn():
    assert find2020TwoEntriesProductIn(_expenses) == TEST_MAGIC_PRODUCT_TWO


def test_find2020ThreeEntriesProductIn():
    assert find2020ThreeEntriesProductIn(_expenses) == TEST_MAGIC_PRODUCT_THREE


def test_main():
    assert main(TEST_EXPENSES_FILE_NAME) == (TEST_MAGIC_PRODUCT_TWO, TEST_MAGIC_PRODUCT_THREE)

