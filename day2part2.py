#More info: https://adventofcode.com/2020/day/2

with open("inputDay2.txt") as _file:
    values = [str(line) for line in _file]

total = 0
for i in range(len(values)):        
        for j in range(len(values[i])):
            evaluated = values[i].split(' ')            
        frequency = evaluated[0].split('-') 
        character = evaluated[1].replace(':','')
        text = evaluated[2]
        if (character == text[int(frequency[0])-1] and character != text[int(frequency[1])-1] and text[int(frequency[0])-1] != text[int(frequency[1])-1]) or (character != text[int(frequency[0])-1] and character == text[int(frequency[1])-1] and text[int(frequency[0])-1] != text[int(frequency[1])-1]): #take care with zero position!!
            total+=1
print(total)
  
