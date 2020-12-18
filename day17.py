def generateNeighbors(x,y,z):
    x_list = [x-1, x, x+1]
    y_list = [y-1, y, y+1]
    z_list = [z-1, z, z+1]
    neighbors = []
    for h in x_list:
        for j in y_list:
            for k in z_list:
                neighbors.append((h,j,k))
    neighbors.remove((x,y,z))
    return neighbors

def checkActiveNeighbors(x,y,z):
    neighbors = generateNeighbors(x,y,z)
    currentactive = 0
    for iterator in neighbors:
        if iterator in activecubes:
            currentactive = currentactive + 1
    return currentactive

if __name__ == '__main__':
    with open("inputDay17.txt") as f:
        data = f.read().split("\n")

    activecubes = [] #store the current active cubes

    for iterY,row in enumerate(data):
        for iterX, val in enumerate(list(row)):
            if val == '#':
                activecubes.append((iterX, iterY, 0))

    rounds = 6
    for i in range(rounds):
        potentialcubes = list(activecubes)
        for itercube in activecubes:
            potentialcubes = potentialcubes + generateNeighbors(itercube[0], itercube[1], itercube[2])
        potentialcubes = list(set(potentialcubes))
        
        new_activecubes = []
        for itercube in potentialcubes:
            activeneighbors = checkActiveNeighbors(itercube[0], itercube[1], itercube[2])
            if itercube in activecubes:
                if activeneighbors == 2 or activeneighbors == 3:
                    new_activecubes.append(itercube)
            else:
                if activeneighbors == 3:
                    new_activecubes.append(itercube)
        activecubes = new_activecubes
    print(len(activecubes))
