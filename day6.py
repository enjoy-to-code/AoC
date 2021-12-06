from collections import defaultdict

test = False
filename = "test.txt" if test else "input.txt"

with open(filename, "r") as data:
    initial_state = data.read().strip().split(',')

# brute force
def solveA(n):
    values = [int(x) for x in initial_state]
    for day in range(n):
        print("Day:", day)
        i=0
        newFish = 0
        for x in values:
            if x==0:
                values[i] = 6
                newFish += 1
            else:
                values[i] = x-1
            i+=1
        for n in range(newFish):
            values.append(int(8))
    print(len(values))

# using frequency counting
def solveB(days):
    answer = 0
    freq = defaultdict(int)
    
    for i in initial_state:
        freq[int(i)] += 1

    for _ in range(days):
        new_freq = defaultdict(int)
        for key in freq:
            if key == 0:
                new_freq[6] += freq[key]
                new_freq[8] = freq[key]
            else:
                new_freq[key-1] += freq[key]

        freq = new_freq
    for key in freq:
        answer += freq[key]
    print(answer)

solveA(80) # 358214 
solveB(256) # 1622533344325
