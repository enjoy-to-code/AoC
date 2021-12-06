with open("input.txt", "r") as data:
    lines = data.read().split("\n")

boards = []
numbers = []
board = []
values = []
marked = []
marker = []

for line in lines:
    line = line.strip()
    if not numbers == []:
        numbers = [int(x) for x in line.split(',')]
    else:
        if line:
            board.append( [int(x) for x in line.split()] )
            marker.append( [False for _ in range(5)] )
        else:
            if board:
                boards.append(board)
                marked.append(marker)
            #board.clear()
            board = []
            marker = []
boards.append(board)
marked.append(marker)

def printBoard(nr):
    for r in range(5):
        for c in range(5):
            if marked[nr][r][c] == False:
                print("\033[1;37m", boards[nr][r][c], end=" " )
            else:    
                print("\033[1;32m", boards[nr][r][c], end=" " )
        print()


def checkForBingo():
    for i in range(len(boards)):
        for r in range(5):
            cnt = 0
            for c in range(5):
                if marked[i][r][c]:
                    cnt += 1
            if (cnt == 5):
                return True
        for c in range(5):
            cnt = 0
            for r in range(5):
                if marked[i][r][c]:
                    cnt += 1
            if (cnt == 5):
                return True
    return False        

def checkBoardForBingo(b):
    for r in range(5):
        cnt = 0
        for c in range(5):
            if marked[b][r][c]:
                cnt += 1
        if (cnt == 5):
            return True
    
    for c in range(5):
        cnt = 0
        for r in range(5):
            if marked[b][r][c]:
                cnt += 1
        if (cnt == 5):
            return True
    return False        
    

def findBingo():
    for num in numbers:
        for i in range(len(boards)):
            for r in range(5):
                for c in range(5):
                    if boards[i][r][c] == num:
                        marked[i][r][c] = True
                        if checkForBingo():    
                            return num, i


def partA():
    num, boardnr = findBingo()    
    sum = 0

    for r in range(5):
        for c in range(5):
            if marked[boardnr][r][c] == False:
                sum += boards[boardnr][r][c]     
    
    print(num * sum)


def partB():
    nr_brds = len(boards)
    boardnr = 0
    sum = 0
    number = 0
    board_ready  = [False for i in range(len(boards))]
    for num in numbers:
        #print('NUM: ', num)
        for i in range(len(boards)):
            for r in range(5):
                for c in range(5):
                    if boards[i][r][c] == num:
                        marked[i][r][c] = True
                        if board_ready[i] == False:
                            if checkBoardForBingo(i):    
                                #print("Board: ", i, "BINGO!", num)
                                board_ready[i] = True
                                if board_ready.count(True) == nr_brds:
                                    boardnr = i
                                    number = num
                                    printBoard(i)                                            
                                    for r in range(5):
                                        for c in range(5):
                                            if marked[boardnr][r][c] == False:
                                                sum += boards[boardnr][r][c]     
                                    print(sum*number)


partA()  # 41503
partB()  # 3178