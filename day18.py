#https://adventofcode.com/2020/day/18

def analyze(string):
    if "(" in string:
        openparenthesis = 0
        first = string.index("(")
        for i in range(first, len(string)):
            if string[i] == "(":
                openparenthesis += 1
            elif string[i] == ")":
                openparenthesis -= 1
            if openparenthesis == 0:
                break
        return analyze(string[:first] + str(analyze(string[first + 1 : i])) + string[i + 1 :])

    else:
        grams = string.split(" ")
        total = int(grams[0])
        for i in range(1, len(grams), 2):
            total = eval(f"{total} {grams[i]} {grams[i+1]}")
        return total
        
    


if __name__ == '__main__':    
    with open("inputDay18.txt") as f:
        data = f.readlines()
        
    total = sum([analyze(l) for l in data])
    print(total)
