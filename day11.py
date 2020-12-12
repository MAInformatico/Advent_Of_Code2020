
def countChairs(values):
    lenMatrix = len(values)
    lenRow = len(values[0])
    adjacents = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    next_values = [["x" for c in r] for r in values]
    
    while True:
        changed = False
        for i in range(lenMatrix):
            for j in range(lenRow):
                num_occ = sum([values[i + y][j + x] == "#" for x, y in adjacents if 0 <= i + y < lenMatrix and 0 <= j + x < lenRow])

                if values[i][j] == "L" and num_occ == 0:
                    next_values[i][j] = "#"
                    changed = True
                elif values[i][j] == "#" and num_occ >= 4:
                    next_values[i][j] = "L"
                    changed = True
                else:
                    next_values[i][j] = values[i][j]

        if not changed: break
        values = [[next_values[i][j] for j in range(lenRow)] for i in range(lenMatrix)]

    return sum([sum([values[i][j] == "#" for j in range(lenRow)]) for i in range(lenMatrix)])

if __name__ == '__main__':    
    with open("inputDay11.txt") as _file:
        values = list(map(str.strip, _file.readlines()))      
    print(countChairs(values))
