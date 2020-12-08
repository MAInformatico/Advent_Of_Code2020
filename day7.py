#More info: https://adventofcode.com/2020/day/7
import collections

def getAllBags(lines):
    rules = collections.defaultdict(list)
    for it in lines:
        left, right = it.split(' contain ')
        keys = cleaner(left)
        for colors in right.split(','):
            contained = cleaner(colors[2:])
            rules[contained].append(keys)
    return len(filterbyColor(rules, 'shiny gold'))


def cleaner(color):
    return color.replace(' bags', '').replace(' bag', '').replace('.', '').strip()


def filterbyColor(data, color):
    result = set(data[color])
    for column in data[color]:
        result = result.union(filterbyColor(data, column))
    return result

if __name__ == '__main__':
    with open("inputDay7.txt") as _file:
        values = [str(line) for line in _file]
    print(getAllBags(values))
