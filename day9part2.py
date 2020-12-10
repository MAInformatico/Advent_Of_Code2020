def checker(i, numbers):
    target = numbers[i]
    prevNum = numbers[i-25: i]
    if prevNum.count(target/2) > 1:
        return True
    prevSet = set(prevNum)
    prevSet.discard(target/2)
    for iterator in prevSet:
        if target-iterator in prevSet:
            return True
    return False

def findNumber(numbers):
    for i in range(25, len(numbers)):
        if not checker(i, numbers):
            return numbers[i]

def weakness(numbers):
    target = findNumber(numbers)
    for i, num in enumerate(numbers):
        aux = [num]
        next = i+1
        while sum(aux) < target:
            aux.append(numbers[next])
            next += 1
        if len(aux) >= 2 and sum(aux) == target:
            return min(aux) + max(aux)

def main():
    with open("inputDay9.txt", 'r') as _file:
        numbers = list(map(int, _file.read().splitlines()))
    print(weakness(numbers))
main()

