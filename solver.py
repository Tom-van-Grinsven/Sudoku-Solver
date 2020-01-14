import urllib.request, json

def get_board():
    with urllib.request.urlopen("https://sugoku.herokuapp.com/board?difficulty=easy") as url:
        data = json.loads(url.read().decode())
        return data["board"]

board = get_board()

# board = [
#     [0,0,3,7,0,0,0,6,0],
#     [0,0,0,5,6,0,0,4,0],
#     [0,6,2,0,0,0,7,0,8],
#     [0,9,7,3,8,0,6,0,0],
#     [0,8,0,6,0,0,0,9,0],
#     [0,0,5,4,0,7,0,0,0],
#     [1,0,0,0,0,0,2,0,0],
#     [8,0,0,0,0,0,0,3,9],
#     [0,5,6,0,3,0,0,0,0]
# ]

def print_board(board):
    # traverse the rows
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - - - ")

        # traverse the columns within the row
        for column in range(len(board[0])):
            if column % 3 == 0 and column != 0:
                print(" | ", end="")

            if column == 8:
                print(board[row][column])
            else:
                print(str(board[row][column]) + " ", end="")


def find_next_empty_place(board):
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == 0:
                return row, column

    return None


def is_valid(board, number, position):
    # traverse the row
    for i in range(len(board[0])):
        # if two of the same numbers are in the row (without checking the current inserted number), the board is not valid
        if board[position[0]][i] == number and position[1] != i:
            return False

    # traverse the column
    for i in range(len(board)):
        # if two of the same numbers are in the column (without checking the current inserted number), the board is not valid
        if board[i][position[1]] == number and position[0] != i:
            return False

    # traverse the boxes
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number and (i,j) != position:
                return False

    return True


def solve_sudoku(board):
    # if we hit the end of the board, the solution is found

    found = find_next_empty_place(board)
    if not found:
        return True
    else:
        row, column = found

    for i in range(1, 10):
        if is_valid(board, i, (row, column)):
            board[row][column] = i

            if solve_sudoku(board):
                return True

            board[row][column] = 0

    return False

def print_process():
    print("Board before solving: ")
    print("\n")
    print_board(board)
    print("\n")
    print("Solving")
    print("\n")
    solve_sudoku(board)
    print("Board after solving: ")
    print("\n")
    print_board(board)

print_process()