import numpy as np

test = False
filename = "test.txt" if test else "input.txt"

with open(filename) as data:
    values = data.read().strip().split("\n")
    height_map = [[int(i) for i in list(line)] for line in values]

max_rows = len(height_map)
max_cols = len(height_map[0])

def partA():
    answer = 0
    for row in range(max_rows):
        for col in range(max_cols):
            low = True
            for d in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                rr = row + d[0]
                cc = col + d[1]
                if not ((0 <= rr and rr < max_rows) and (0 <= cc and cc < max_cols)):
                    continue
                if height_map[rr][cc] <= height_map[row][col]:
                    low = False
                    break
            if low:
                answer += height_map[row][col] + 1
    print(answer)


def partB():
    low = []
    cur_id = 1
    ids = np.zeros((max_rows, max_cols), dtype=int)
    # Find low points
    for row in range(max_rows):
        for col in range(max_cols):
            is_low = True
            for d in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                rr = row + d[0]
                cc = col + d[1]

                if not ((0 <= rr and rr < max_rows) and (0 <= cc and cc < max_cols)):
                    continue

                if height_map[rr][cc] <= height_map[row][col]:
                    is_low = False
                    break

            if is_low:
                low.append((row, col))

    for row, col in low:
        stack = [(row, col)]
        visited = set()
        while len(stack) > 0:
            row, col = stack.pop()
            if (row, col) in visited:
                continue
            visited.add((row, col))
            ids[row, col] = cur_id
            for d in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                rr = row + d[0]
                cc = col + d[1]
                if not ((0 <= rr and rr < max_rows) and (0 <= cc and cc < max_cols)):
                    continue
                if height_map[rr][cc] == 9:
                    continue
                stack.append((rr, cc))
        cur_id += 1
    # Find the sizes of biggest basins
    sizes = [0] * cur_id
    for x in ids.flatten():
        sizes[x] += 1
    sizes = sizes[1:]
    sizes.sort()
    print(sizes[-1] * sizes[-2] * sizes[-3])

partA() # 491
partB() # 1075536