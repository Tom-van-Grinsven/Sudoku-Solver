board = [
    [0,0,3,7,0,0,0,6,0],
    [0,0,0,5,6,0,0,4,0],
    [0,6,2,0,0,0,7,0,8],
    [0,9,7,3,8,0,6,0,0],
    [0,8,0,6,0,0,0,9,0],
    [0,0,5,4,0,7,0,0,0],
    [1,0,0,0,0,0,2,0,0],
    [8,0,0,0,0,0,0,3,9],
    [0,5,6,0,3,0,0,0,0]
]

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
                return (row, column)

    return None

print_board(board)