with open("input.txt", "r") as data:
    lines = data.read().split("\n")

def partA():
    hp = 0
    depth = 0

    for line in lines:
        dir = line.split(' ')
        if dir[0] == 'forward':
            hp = hp + int(dir[1])
        elif dir[0] == 'down':
            depth = depth - int(dir[1])
        elif dir[0] == 'up':
            depth = depth + int(dir[1])
    print(hp*abs(depth))   

def partB():
    hp = 0
    depth = 0
    aim = 0

    for line in lines:
        dir = line.split(' ')
        if dir[0] == 'forward':
            hp = hp + int(dir[1])
            depth = depth + aim * int(dir[1])
        elif dir[0] == 'down':
            aim = aim - int(dir[1])
        elif dir[0] == 'up':
            aim = aim + int(dir[1])
    print(hp*abs(depth))   

partA() # 2019945
partB() # 1599311480
