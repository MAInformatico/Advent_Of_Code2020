#https://adventofcode.com/2020/day/8

def asminterpreter(code):
  flag = False
  visited = set()
  ptr = acc = 0
  while ptr < len(code):
    op, value = code[ptr]
    if ptr in visited:
      flag = True
      break
    visited.add(ptr)
    if op == 'jmp':
      ptr = ptr + value
      continue
    elif op == 'acc':
      acc = acc + value
    ptr = ptr + 1
  return (acc, flag)


if __name__ == '__main__':    
    values = []
    with open('inputDay8.txt') as file:
        for line in file:
            line = line.rstrip().split(' ')
            values.append([line[0], int(line[1])])
    asminterpreter(values)
    
    swapDict = {'nop':'jmp','jmp':'nop'}
    for i, (op,value) in enumerate(values):
        if op == 'nop' or op == 'jmp':
            swappedOp = [(swapDict[op], value)]
            newInstructions = values[:i] + swappedOp + values[i+1:]
            accValue, hasLoop = execute(newInstructions)
            if not hasLoop:
                print(accValue)
