#https://adventofcode.com/2020/day/10

import functools

@functools.lru_cache(maxsize=None)
def combinations(n):
    if n == values[-1]:
        return 1
    else:
        if n not in values:
            return 0
        else:
            return combinations(n+1) + combinations(n+2) + combinations(n+3)


def getMultiplyNDifferences(values):
    for i in range(len(values)-1):
        values[i] = values[i+1] - values[i]
    
    return (values.count(3) * values.count(1))


if __name__ == '__main__':    
    with open("inputDay10.txt") as _file:
        values = [int(line) for line in _file]
        values = [0] + values + [max(values)+3]
        values.sort()
        
        #print(getMultiplyNDifferences(values))        
        print(combinations(values[0]))
