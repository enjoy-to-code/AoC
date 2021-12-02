with open("input.txt", "r") as data:
    lines = data.read().split("\n")

def partA():
    hp = 0
    depth = 0

    for line in lines:
        cmd, val = line.split()
        val = int(val)
        if cmd == 'forward':
            hp = hp + val
        elif cmd == 'down':
            depth = depth - val
        elif cmd == 'up':
            depth = depth + val
    print(hp*abs(depth))   

def partB():
    hp = 0
    depth = 0
    aim = 0

    for line in lines:
        cmd, val = line.split()
        val = int(val)
        if cmd == 'forward':
            hp = hp + val
            depth = depth + aim * val
        elif cmd == 'down':
            aim = aim - val
        elif cmd == 'up':
            aim = aim + val
    print(hp*abs(depth))   

partA() # 2019945
partB() # 1599311480
