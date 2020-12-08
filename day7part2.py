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

def getRules(lines):
    rules = collections.defaultdict(list)
    for line in lines:
        left, right = line.split(' contain ')
        holder = cleaner(left)
        for contents in right.split(','):
            contained = cleaner(contents)
            rules[holder].append(contained)
    return countBags(rules, 'shiny gold')


def countBags(data, color):
    if color == 'other':
        return 0
    count = 0
    for iterator in data[color]:
        aux = iterator.split()[0]
        if aux == 'no':
            num = 0
        else:
            num = int(aux)
        col = iterator.split(maxsplit=1)[1]
        count += num * (countBags(data, col) + 1)
    return count



if __name__ == '__main__':
    with open("inputDay7.txt") as _file:
        values = [str(line) for line in _file]
    print(getRules(values))
