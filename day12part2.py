# https://adventofcode.com/2020/day/12 


def calculateWaypoint(f):
    total_EastWest = 0
    total_NorthSouth = 0
    EastWest = 10
    NorthSouth = 1

    for i in f:
        action = i[0]
        num = int(i[1:]) 

        if action == "F":
            total_NorthSouth += (NorthSouth * num)
            total_EastWest += (EastWest * num) 
        elif action == "N":
            NorthSouth += num
        elif action == "S":
            NorthSouth -= num
        elif action == "E":
            EastWest += num
        elif action == "W":
            EastWest -= num

        elif action == "L" and num == 90 or action == "R" and num == 270:
            NorthSouth, EastWest = EastWest, -NorthSouth
        elif action == "L" and num == 270 or action == "R" and num ==90:
            NorthSouth, EastWest = -EastWest, NorthSouth
        elif action == "L" and num == 180 or action == "R" and num == 180:
            NorthSouth = -NorthSouth
            EastWest = -EastWest

    return int(abs(total_EastWest) + abs(total_NorthSouth))


def calculate(f):
    EastWest = 0
    NorthSouth = 0
    direction = 90

    for i in f:
        action = i[0]
        num = int(i[1:])
        if action == "F" and direction == 90 or action == "E":
            EastWest += num
        elif action == "F" and direction == 180 or action == "S":
            NorthSouth -= num
        elif action == "F" and direction == 270 or action == "W":
            EastWest -= num
        elif action == "F" and direction == 0 or action == "N":
            NorthSouth += num
        #Turn to left or right based on ship's facing
        elif action == "L":
            direction -= num
            if direction == 360 or direction == -360:
                direction = 0
            if direction == -90:
                direction = 270
            if direction == -180 or direction == 540:
                direction = 180
            if direction == -270 or direction == 450:
                direction = 90

        elif action == "R":
            direction += num
            if direction == 360 or direction == -360:
                direction = 0
            if direction == -90:
                direction = 270
            if direction == -180 or direction == 540:
                direction = 180
            if direction == -270 or direction == 450:
                direction = 90

    return int(abs(EastWest) + abs(NorthSouth))


if __name__ == '__main__':    
    with open("inputDay12.txt") as f:
        #print(str(calculate(f)))
        print(str(calculateWaypoint(f)))
    
        
        
