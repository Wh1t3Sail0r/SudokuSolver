import pprint

board = [[]]

def findEmpty(board):
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == 0:
                return (x, y)

    return None

def solve(board):
    find = findEmpty(board)
    if find:
        row, col = find
    else:
        return True

    for i in range(1, 10):
        if validPos(board, (row, col), i):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

def validPos(board, pos, value):

    # Check if value is not in row
    for i in range(0, len(board)):
        if board[pos[0]][i] == value and pos[1] != i:
            return False

    # Check if value is not in column
    for i in range(0, len(board)):
        if board[i][pos[1]] == value and pos[1] != i:
            return False

    # Check if value is not in box
    x = pos[1]//3
    y = pos[0]//3

    for i in range(y * 3, y * 3 + 3):
        for j in range(x * 3, x * 3 + 3):
            if board[i][j] == value and (i, j) != pos:
                return False

    return True


if __name__ == '__main__':
    board = [[7, 8, 0, 4, 0, 0, 1, 2, 0],
             [6, 0, 0, 0, 7, 5, 0, 0, 9],
             [0, 0, 0, 6, 0, 1, 0, 7, 8],
             [0, 0, 7, 0, 4, 0, 2, 6, 0],
             [0, 0, 1, 0, 5, 0, 9, 3, 0],
             [9, 0, 4, 0, 6, 0, 0, 0, 5],
             [0, 7, 0, 3, 0, 0, 0, 1, 2],
             [1, 2, 0, 0, 0, 7, 4, 0, 0],
             [0, 4, 9, 2, 0, 6, 0, 0, 7]]

    p = pprint.PrettyPrinter(width = 41, compact = True)
    solve(board)
    p.pprint(board)



