test = False
filename = "test.txt" if test else "input.txt"

values = []

def read_data():
    for line in open(filename):
        values.append([int(x) for x in line.strip()])    

def flash(r, c):
    number_flashes = 1
    values[r][c] = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if 0 <= r+dr < 10 and 0 <= c+dc < 10 and values[r+dr][c+dc] !=0:
                values[r+dr][c+dc] += 1
                if values[r+dr][c+dc] > 9:
                    number_flashes += flash(r+dr, c+dc)
    return number_flashes

def partA():
    count_flashes = 0
    for x in range(100):
        for r in range(10):
            for c in range(10):
                values[r][c] += 1
        for r in range(10):
            for c in range(10):
                if values[r][c] > 9:
                    count_flashes += flash(r,c)
    print(count_flashes)

def partB():
    x = 0
    while True:
        count_flashes = 0
        for r in range(10):
            for c in range(10):
                values[r][c] += 1
        for r in range(10):
            for c in range(10):
                if values[r][c] > 9:
                    count_flashes += flash(r,c)
        x += 1
        if count_flashes == 100:
            print(x)
            break

read_data()
partA() 
values = []
read_data()
partB() 