from collections import deque

test = False
filename = "test.txt" if test else "input.txt"

with open(filename, "r") as data:
    lines = data.read().split("\n")

closing = [')', ']', '}', '>']

def partA():
    stack = deque() 
    answer = 0
    for line in lines:
        for c in line:
            if c not in closing:
                stack.append(c)
            else:
                if c == ')':
                    prev = stack.pop()
                    if prev == '(':
                        continue
                    else:
                        answer += 3
                elif c == ']':
                    prev = stack.pop()
                    if prev == '[':
                        continue
                    else:
                        answer += 57
                elif c == '}':
                    prev = stack.pop()
                    if prev == '{':
                        continue
                    else:
                        answer += 1197
                elif c == '>':
                    prev = stack.pop()
                    if prev == '<':
                        continue
                    else:
                        answer += 25137
    print(answer)

def partB():
    answer = 0
    points = {'(':1, '[':2, '{':3, '<':4}
    scores = []
    for line in lines:
        stack = deque() 
        corrupted = False
        for c in line:
            if c not in closing:
                stack.append(c)
            else:
                if c == ')':
                    prev = stack.pop()
                    if prev == '(':
                        continue
                    else:
                        corrupted = True
                elif c == ']':
                    prev = stack.pop()
                    if prev == '[':
                        continue
                    else:
                        corrupted = True
                elif c == '}':
                    prev = stack.pop()
                    if prev == '{':
                        continue
                    else:
                        corrupted = True
                elif c == '>':
                    prev = stack.pop()
                    if prev == '<':
                        continue
                    else:
                        corrupted = True
        if not corrupted:
            val = 0
            for c in reversed(stack):
                val = val * 5 + points[c]
            scores.append(val)
    scores.sort()
    answer = scores[len(scores)//2]
    print(answer)

partA() #316851
partB() #2182912364