'''
This module is designed to check if the game board is ready to play

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
    and False otherwise

    '''
    if symb in [' ', '*']:
        return True

    if symb not in used:
        used.append(symb)
        return True

    return False

def check_row(board: list, row: int) -> bool:
    '''
    Check if the symbols in a given row are unique or ' ', '*'

    '''

    used = []
    for col in range(len(board)):
        if not check_cell(board[row][col], used):
            return False

    return True

def check_col(board:list, col: int) -> bool:
    '''
    Check if the symbols in a given column are unique or ' ', '*'

    '''

    used = []
    for row in range(len(board)):
        print(used)
        if not check_cell(board[row][col], used):
            return False

    return True



if __name__ == "__main__":
    print(check_col(EXAMPLE, 4))

