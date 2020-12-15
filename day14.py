# https://adventofcode.com/2020/day/14

import re
import sys

word = 36
mask_regexp   = r'mask = (.*)'
memory_regexp = r'mem\[(\d+)\] = (\d+)'

def getMaskValue(mask, value):
    return ''.join([
        v if m == 'X' else m for m, v in zip(mask, value)
    ])

def intToBinary(i):
    return format(int(i), f'0{word}b')

def readFile():
    memory = {}
    mask   = '0'*word

    for iterator in sys.stdin: #read file from shell
        if iterator.startswith('mask'): # https://www.w3schools.com/python/ref_string_startswith.asp
            mask = re.findall(mask_regexp, iterator)[0]
        else:
            address, value  = re.findall(memory_regexp, iterator)[0]
            memory[address] = getMaskValue(mask, intToBinary(value))

    return memory


if __name__ == '__main__':
    memory = readFile()
    result  = sum(int(v, 2) for v in memory.values())

    print(result)
