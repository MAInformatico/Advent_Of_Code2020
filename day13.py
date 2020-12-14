# https://adventofcode.com/2020/day/13

import re

def find_multiples(number,value):
  multiples=[]
  for i in range(number//value+1, number//value+2):
    multiples.append(i*value)

  return multiples

def findEarliestDeparture(buses):
    departure={}                 
    for x in buses:
        if (''.join(re.findall('[0-9]', x))) != '':
            departure.update({x:find_multiples(time,int(x))})

    minValue = int(min(departure, key=departure.get))       
    maxValue = min(departure.values())[0]                   

    print((maxValue-time)*minValue)
    
    
if __name__ == '__main__':
    input = open('inputDay13.txt')
    values = input.read().split('\n')
    values[1] = values[1].split(',')
    time = int(values[0])
    buses = values[1]    
    findEarliestDeparture(buses)
    
