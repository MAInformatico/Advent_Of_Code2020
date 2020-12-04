#More info: https://adventofcode.com/2020/day/4

def checkPassports(values):
    totalChecked = 0
    dictPassport = {"byr": {"min": 1920, "max": 2002}, "iyr": {"min": 2010, "max": 2020}, "eyr": {"min": 2020, "max": 2030}, "hgt": {"cm":{"min": 150, "max":193}, "in":{"min":59, "max":76}},"hcl": "","ecl": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],"pid": ""}
    for i in values:
        if all((x in i) for x in dictPassport):
            try:
                if (dictPassport["byr"]["min"] <= int(i.split("byr:")[1][:4]) <= dictPassport["byr"]["max"]
                    and 
                    dictPassport["iyr"]["min"] <= int(i.split("iyr:")[1][:4]) <= dictPassport["iyr"]["max"]
                    and 
                    dictPassport["eyr"]["min"] <= int(i.split("eyr:")[1][:4]) <= dictPassport["eyr"]["max"]
                    and 
                    (dictPassport["hgt"][i.split("hgt:")[1].rsplit()[0][-2:]]["min"] <= int(i.split("hgt:")[1].rsplit()[0][:-2]) <= dictPassport["hgt"][i.split("hgt:")[1].rsplit()[0][-2:]]["max"])
                    and
                    i.split("hcl:")[1][0] == "#" and int(i.split("hcl:")[1][1:7], 16) is not ValueError and i.split("ecl:")[1][:3] in dictPassport["ecl"] and int(i.split("pid:")[1].rsplit()[0]) is not ValueError and len(i.split("pid:")[1].rsplit()[0]) == 9
                    ): 
                        totalChecked += 1
            except:
                continue
    return totalChecked

def main():
    with open("inputDay4.txt") as f:
        values = f.read().split("\n\n")
    totalChecked = checkPassports(values)
    print(totalChecked)

if __name__ == "__main__":
    main()
