# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from aoc.day_18_evalexp import _evaluateExpression
from aoc.day_18_evalexp import _tokenizeExpression
from aoc.day_18_evalexp import loadExerciseDataFrom
from aoc.day_18_evalexp import main
from aoc.day_18_evalexp import resolvePuzzleUsing


# +++ constants +++

TEST_DAY_18_EVALEXP_FILE_NAME = 'resources/test/day_18_evalexp-test-data.txt'


# +++ tests +++

_data, _tokens = loadExerciseDataFrom(TEST_DAY_18_EVALEXP_FILE_NAME)


def test__tokenizeExpression():
    test = '2 * 3 + (4 * 5)'
    
    tokens = _tokenizeExpression(test)

    assert tokens[1] == '*'
    assert tokens[4] == '('
    assert tokens[8] == ')'


def test__evaluateExpression():
    test = '2 * 3 + 4 * 5'
    result, _ = _evaluateExpression(_tokenizeExpression(test), False)
    assert 50 == result

    test = '2 * 3 + (4 * 5)'
    result, _ = _evaluateExpression(_tokenizeExpression(test), False)
    assert 26 == result

    test = '1 + (2 * 3) + (4 * (5 + 6))'
    result, _ = _evaluateExpression(_tokenizeExpression(test), False)
    assert 51 == result

    test = '5 + (8 * 3 + 9 + 3 * 4 * 3)'
    result, _ = _evaluateExpression(_tokenizeExpression(test), False)
    assert 437 == result

    test = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'
    result, _ = _evaluateExpression(_tokenizeExpression(test), False)
    assert 12240 == result

    test = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
    result, _ = _evaluateExpression(_tokenizeExpression(test), False)
    assert 13632 == result


def test__evaluateExpressionReversePrecedence():
    test = '1 + 2 * 3 + 4 * 5 + 6'
    result, _ = _evaluateExpression(_tokenizeExpression(test))
    assert 231 == result

    test = '2 * 3 + (4 * 5)'
    result, _ = _evaluateExpression(_tokenizeExpression(test))
    assert 46 == result

    test = '1 + (2 * 3) + (4 * (5 + 6))'
    result, _ = _evaluateExpression(_tokenizeExpression(test))
    assert 51 == result

    test = '5 + (8 * 3 + 9 + 3 * 4 * 3)'
    result, _ = _evaluateExpression(_tokenizeExpression(test))
    assert 1445 == result

    test = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'
    result, _ = _evaluateExpression(_tokenizeExpression(test))
    assert 669060 == result

    test = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
    result, _ = _evaluateExpression(_tokenizeExpression(test))
    assert 23340 == result


def test_resolvePuzzleUsing():
    answer = resolvePuzzleUsing(_data, _tokens, False)
    assert answer == 26386

    answer = resolvePuzzleUsing(_data, _tokens, True)
    assert answer == 693942


def test_main():
    assert main(TEST_DAY_18_EVALEXP_FILE_NAME) == (26386, 693942)


test_resolvePuzzleUsing()

