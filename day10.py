#https://adventofcode.com/2020/day/10

def getMultiplyNDifferences(values):
    for i in range(len(values)-1):
        values[i] = values[i+1] - values[i]
    
    return (values.count(3) * values.count(1))

if __name__ == '__main__':    
    with open("inputDay10.txt") as _file:
        values = [int(line) for line in _file]
        values = [0] + values + [max(values)+3]
        values.sort()
            
        print(getMultiplyNDifferences(values))
