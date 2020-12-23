#https://adventofcode.com/2020/day/22

from collections import deque
from copy import deepcopy #https://docs.python.org/3/library/copy.html

def play(numericValues):
    while all(player for player in numericValues):
        games = [player.popleft() for player in numericValues]
        winner = max((value, ind) for (ind, value) in enumerate(games))
        numericValues[winner[1]].extend(sorted(games, reverse=True))

    return max(calculateScore(player) for player in numericValues)

def filtering(data):
    numericValues = [deque()]
    flag = 0
    with open(data, "r") as f:
        for iterator in f:
            iterator = iterator.strip()

            if iterator.isnumeric():
                numericValues[flag].append(int(iterator))
                continue

            if not iterator:
                flag += 1
                numericValues.append(deque())

    return numericValues

def calculateScore(winner):
    return sum(value * index for index, value in enumerate(reversed(winner), start=1))

if __name__ == '__main__':        
    data = filtering("inputDay22.txt")            
    print(play(deepcopy(data))) 
    
    
