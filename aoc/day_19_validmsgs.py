# BSD-3 - See: https://github.com/pr3d4t0r/aoc2020/blob/master/LICENSE.txt
# vim: set fileencoding=utf-8:


from util import loadExerciseDataFrom
from util import mainStart


# +++ constants +++


# *** functions ***

def _parseRuleFrom(item):
    r = item.split(':')
    k = int(r[0].strip())
    v = list()

    for ruleGroup in [ruleGroup.split() for ruleGroup in [ruleTxt.strip() for ruleTxt in r[1].split('|')]]:
        if any('"' in rule for rule in ruleGroup):
            v = [rule.replace('"', '') for rule in ruleGroup][0]
        else:
            v.append([int(rule) for rule in ruleGroup])
    
    return k, v


def _rulesAndMessagesFrom(data):
    rules = dict()
    messages = list()
    state = 0

    for seq, item in enumerate(data):
        if state == 0 and item:
            r = _parseRuleFrom(item)
            rules[r[0]] = r[1]
        elif not item:
            state = 1
        elif state == 1 and item:
            messages.append(item)

    return rules, messages


def _process(message, ruleNumber, rules):
    if isinstance(rules[ruleNumber], list):
        canary = list()
        for ruleSet in rules[ruleNumber]:
            subMessage1 = [message,]
            for rule in ruleSet:
                subMessage2 = list()
                for symbol in subMessage1:
                    subMessage2 += _process(symbol, rule, rules)
                subMessage1 = subMessage2
                if not subMessage1:
                    break
            if subMessage1:
                canary += subMessage1
        return canary
    else:
        if message and message[0] == rules[ruleNumber]:
            return [message[1:]]

    return list()


def resolvePuzzle01Using(data, tokens):
    rules, messages = _rulesAndMessagesFrom(data)

    answer = sum('' in _process(message, 0, rules) for message in messages)

    return answer, rules, messages


def resolvePuzzle02Using(rules, messages):
    rules[8] = [[42], [42, 8],]
    rules[11] = [[42, 31,], [42, 11, 31],]

    answer = sum('' in _process(message, 0, rules) for message in messages)

    return answer


def main(fileName:str = None):
    fileName = mainStart(fileName, 19)

    data, tokens = loadExerciseDataFrom(fileName)

    answer1, rules, messages = resolvePuzzle01Using(data, tokens)
    print('answer 1: %d' % answer1)

    answer2 = resolvePuzzle02Using(rules, messages)
    print('answer 2: %d' % answer2)

    return answer1, answer2


# --- main ---

if '__main__' == __name__:
    main()

