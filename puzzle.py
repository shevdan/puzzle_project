'''
This module is designed to check if the game board is ready to play

https://github.com/shevdan/puzzle_project
'''

EXAMPLE = [
"**** ****",
 "***1 ****",
 "**  3****",
 "* 4 1****",
 "     9 5 ",
 " 6  83  *",
 "3   1  **",
 "  8  2***",
 "  2  ****"
]


def check_cell(symb: str, used: list) -> bool:
    '''
    Check if the symbol in the cell was already used.
    Returns True if symbol is ' ', '*' or not in used
    and False otherwise. ' ' and '*' are included in visited
    by default so they do not affect the function.

    >>> check_cell(' ', ['1', '*', ' '])
    True
    >>> check_cell('*', ['1', '*', ' '])
    True
    >>> check_cell('1', ['1', '*', ' '])
    False
    '''


    if symb not in used or symb in (' ', '*'):
        used.append(symb)
        return True

    return False

def check_row(board: list, row: int) -> bool:
    '''
    Check if the symbols in a given row are unique or ' ', '*'

    >>> check_row(EXAMPLE, 4)
    True
    >>> check_row(EXAMPLE, 1)
    True
    '''

    used = []
    for col in range(len(board)):
        if not check_cell(board[row][col], used):
            return False

    return True

def check_col(board:list, col: int) -> bool:
    '''
    Check if the symbols in a given column are unique or ' ', '*'

    >>> check_col(EXAMPLE, 4)
    False
    >>> check_col(EXAMPLE, 1)
    True
    '''

    used = []
    for row in range(len(board)):
        if not check_cell(board[row][col], used):
            return False

    return True

def check_color(board:list) -> bool:
    '''
    Check if the symbols in a colored corner 5x5 are unique or ' ' or '*'.
    Colors indexing starts at 0 meaning the leftmost corner of the border.
    If any of the symbols in any of the colors is not unique, returns False

    >>> check_color(EXAMPLE)
    True

    '''

    #board should be at least 5x5 size to contain colored colors
    #max number of colors is size of the board - 4
    num_col = len(board) - 4
    for curr_col in range(num_col):
        used = []
        color_idx = len(board) - curr_col - 1
        corner = board[color_idx][curr_col]
        #adding to the visited corner symbol not to check it twice
        used.append(corner)
        for idx in range(1, 5):
            #check the colored 5 cells in a row, excluding corner cell
            check_idx = curr_col + idx
            if not check_cell(board[color_idx][check_idx], used):
                return False
            #check the colored 5 cells in a column, excluding corner cell
            #len(board) - check_idx reverses the index for column indexation
            if not check_cell(board[color_idx - idx][curr_col], used):
                return False
        return True

def check_board(board: list):
    '''
    Main function for validating the board for the beginning of the game

    >>> check_board(EXAMPLE)
    False
    '''
    size = len(board)
    if check_color(board):
        for idx in range(size):
            if check_col(board, idx) and check_row(board, idx):
                continue
            return False
    return True


if __name__ == "__main__":
    import doctest
    doctest.testmod()

