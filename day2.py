#More info: https://adventofcode.com/2020/day/2

with open("inputDay2.txt") as _file:
    values = [str(line) for line in _file]

total = 0
for i in range(len(values)):        
        for j in range(len(values[i])):
            evaluated = values[i].split(' ')
            
        frequency = evaluated[0].split('-') 
        character = evaluated[1].replace(':','')
        reps = evaluated[2].count(character)
        if reps>=int(frequency[0]) and reps<=int(frequency[1]):
            total+=1
print(total)
  
