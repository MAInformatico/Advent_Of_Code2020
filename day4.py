#More info: https://adventofcode.com/2020/day/4

def checkPassports(values):
    totalValid = 0
    dictPassport = {"byr": 0,"iyr": 0,"eyr": 0,"hgt": 0,"hcl": "","ecl": "", "pid": ""}
    for i in values:
        if all((x in i) for x in dictPassport):
            totalValid += 1            
    return totalValid


def main():
    with open("inputDay4.txt") as f:
        values = f.read().split("\n\n")
    totalValids = checkPassports(values)
    print(totalValids)

if __name__ == "__main__":
    main()
