from collections import defaultdict

test = False
filename = "test.txt" if test else "input.txt"

with open(filename, "r") as data:
    lines = data.read().split("\n")

visited = defaultdict(int)

def partA():
    for start, stop in [line.split(" -> ") for line in lines]:
        x1, y1 = [int(i) for i in start.split(",")]
        x2, y2 = [int(i) for i in stop.split(",")]

        dx = x2-x1
        dy = y2-y1 
        
        for i in range(1+max(abs(dx), abs(dy))):
            if dx>0:
                x= x1 + 1*i
            elif dx<0:
                x= x1 - 1*i
            else:
                x = x1
            
            if dy>0:
                y= y1 + 1*i
            elif dy<0:
                y= y1 - 1*i
            else:
                y= y1

            if dx==0 or dy==0:
                visited[(x,y)] += 1

    print(len([overlap for overlap in visited if visited[overlap]>1]))
    

def partB():
    visited.clear()
    for start, stop in [line.split(" -> ") for line in lines]:
        x1, y1 = [int(i) for i in start.split(",")]
        x2, y2 = [int(i) for i in stop.split(",")]

        dx = x2-x1
        dy = y2-y1 
        
        for i in range(1+max(abs(dx), abs(dy))):
            if dx>0:
                x= x1 + 1*i
            elif dx<0:
                x= x1 - 1*i
            else:
                x = x1
            
            if dy>0:
                y= y1 + 1*i
            elif dy<0:
                y= y1 - 1*i
            else:
                y= y1

            visited[(x,y)] += 1

    print(len([overlap for overlap in visited if visited[overlap]>1]))

partA() #7297 
partB() #103046