from collections import defaultdict, deque

test = False
filename = "test.txt" if test else "input.txt"

adj_list = defaultdict(list)
for line in open(filename):
    x,y = line.strip().split('-')
    adj_list[x].append(y)
    adj_list[y].append(x)

def partA():
    start = ('start', set(['start']))
    answer = 0
    visited = deque([start])
    while visited:
        pos, small_caves = visited.popleft()
        if pos == 'end':
            answer += 1
            continue
        for v in adj_list[pos]:
            if v not in small_caves:
                new_small_caves = set(small_caves)
                if v.lower() == v:
                    new_small_caves.add(v)
                visited.append((v, new_small_caves))
    print(answer)

def partB():
    start = ('start', set(['start']), None)
    answer = 0
    visited = deque([start])
    while visited:
        pos, small_caves, small_caves_second = visited.popleft()
        if pos == 'end':
            answer += 1
            continue
        for v in adj_list[pos]:
            if v not in small_caves:
                new_small_caves = set(small_caves)
                if v.lower() == v:
                    new_small_caves.add(v)
                visited.append((v, new_small_caves, small_caves_second))
            elif v in small_caves and small_caves_second is None and v not in ['start', 'end']:
                visited.append((v, small_caves, v))
    print(answer)

partA() # 3000
partB() # 74222