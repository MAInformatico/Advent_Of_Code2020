with open("inputDay5.txt") as file:
    dictData = []
    for line in file.readlines():
        rowValue = int(line[:7].replace("F", "0").replace("B", "1"), 2)
        columnValue = int(line[7:].replace("L", "0").replace("R", "1"), 2)    
        dictData.append((8 * rowValue) + columnValue)
    missing = (((max(dictData) + min(dictData)) / 2) * (len(dictData) + 1)) - sum(dictData)
    print(str(int(missing)))
