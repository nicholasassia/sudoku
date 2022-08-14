board = [
    [4,2,1,0,0,0,0,0,0],
    [0,0,0,0,3,0,0,8,0],
    [0,7,0,2,9,0,0,0,0],
    [0,0,9,0,0,0,0,0,1],
    [0,5,0,4,0,6,0,3,0],
    [7,0,0,0,0,0,4,0,0],
    [0,0,0,0,5,1,0,7,0],
    [0,3,0,0,7,0,0,0,0],
    [0,0,0,0,0,0,3,2,6]]

def printBoard(board):
    for i in range(0, 9):
        for j in range(0, 9):
            print(board[i][j], end=" ")
        print()

def isPossible(board, row, col, val):
    for j in range(0, 9):
        if board[row][j] == val:
            return False

    for i in range(0, 9):
        if board[i][col] == val:
            return False

    startRow = (row // 3) * 3
    startCol = (col // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if board[startRow+i][startCol+j] == val:
                return False
    return True

def solve():
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                for val in range(1, 10):
                    if isPossible(board, i, j, val):
                        board[i][j] = val
                        solve()
                        board[i][j] = 0
                return
    printBoard(board)

solve()