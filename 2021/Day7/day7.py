import sys

test = False
filename = "test.txt" if test else "input.txt"

with open(filename, "r") as data:
     values = data.read().strip().split(",")

values = [int(i) for i in values]

def partA(answer):
    for i in values:
        cost = 0
        for v in values:
            cost += abs(v - i)
        answer = min(answer, cost)
    print(answer)

def partB(answer):
    for i in values:
        cost = 0
        for v in values:
            dist = abs(v - i)
            tmp_cost = dist * (dist + 1) // 2
            cost += tmp_cost
            #print(i, v, tmp_cost, cost )
        answer = min(answer, cost)
    print(answer)

partA(sys.maxsize) # 351901
partB(sys.maxsize) # 101079875 