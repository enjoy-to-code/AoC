with open("input.txt", "r") as data:
    values = [int(x) for x in open('input.txt')]

def partA():
    total = 0
    for idx in range(len(values)):
        if (idx >= 1) and (values[idx] > values[idx-1]):
            total += 1
    print(total)

def partB():
    total = 0
    for idx in range(len(values)):
        if (idx >= 3) and (values[idx] + values[idx-1] + values[idx-2]) > (values[idx-1] + values[idx-2] + values[idx-3]): 
            total +=1
    print(total)

partA() #1752
partB() #1781