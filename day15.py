#https://adventofcode.com/2020/day/15

def calculateIteration(initialnums,limit):
    iterator = len(initialnums)
    number = initialnums[-1]
    dictnumbers = {}
    for i, v in enumerate(initialnums):
        dictnumbers[v] = i + 1
    
    while iterator < limit:
        if not dictnumbers.get(number, None):
            dictnumbers[number] = iterator
            number = 0
            iterator += 1
        else:
            last_num_pos = dictnumbers[number]
            dictnumbers[number] = iterator
            number = iterator - last_num_pos
            iterator += 1
    
    return number

if __name__ == '__main__':
    initialnums = [20,9,11,0,1,2]    
           
    result = calculateIteration(initialnums,2020)
    print(result)
    again = calculateIteration(initialnums,30000000)
    print(again)
