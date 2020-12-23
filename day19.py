#https://adventofcode.com/2020/day/19

import re

def generateRegex(rule, rules, depth, maxdepth):
    if maxdepth and depth > maxdepth:
        return ""
    if "a" in rule:
        return "a"
    elif "b" in rule:
        return "b"
    elif "|" in rule:
        left, right = re.findall(r'(.+) \| (.+)', rule)[0]
        return "(?:" + generateRegex(left, rules,  depth + 1, maxdepth) + \
            "|" + generateRegex(right, rules,  depth + 1, maxdepth) + ")"
    else:
        regex = ""
        index = re.findall(r'(\d+)', rule)
        for i in index:
            regex += generateRegex(rules[int(i)],
                                    rules,  depth + 1, maxdepth)
        return regex


def Matches(string, regexpression):
    count = 0
    for iterator in string:
        if regexpression.match(iterator):
            count += 1
    return count


if __name__ == '__main__':    

    with open("inputDay19.txt") as f:
        data = f.read()

    rulestext = re.findall(r'(\d+)\: (.+)', data)
    rules = [[]] * (len(rulestext))
    for rule in rulestext:
        rules[int(rule[0])] = rule[1]
    string = re.findall(r'([a|b]\w+)', data)
    
    regexpression = re.compile("^" + generateRegex(rules[0], rules, 0, 0) + "$")
    print(Matches(string, regexpression))
    
