from typing import Final, Union

EMPTY: Final = 0

Board = list[list[int]]
Square = dict[str, int]


def is_num_in_row(num: int, row: int, board: Board) -> bool:
    try:
        board[row].index(num)
        return True
    except ValueError:
        return False


def is_num_in_col(num: int, col: int, board: Board) -> bool:
    for row in board:
        if row[col] == num:
            return True
    return False


def is_num_in_box(num: int, row: int, col: int, board: Board) -> bool:
    s: Square = {"row": (row // 3) * 3, "col": (col // 3) * 3}
    e: Square = {"row": s["row"] + 3, "col": s["col"] + 3}

    for i in range(s["row"], e["row"]):
        for j in range(s["col"], e["col"]):
            if board[i][j] == num:
                return True
    return False


def is_num_ok_in_square(num: int, row: int, col: int, board: Board) -> bool:
    return (
        not is_num_in_row(num, row, board) and
        not is_num_in_col(num, col, board) and
        not is_num_in_box(num, row, col, board)
    )


def find_empty_square(board: Board) -> Union[Square, None]:
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == EMPTY:
                return {"row": i, "col": j}
    return None


def sudoku(board: list[list[int]]) -> bool:
    """
    Solves a given, 9x9 Sudoku board.

    Returns:
        True when sudoku board is solved, False otherwise.
    """
    square = find_empty_square(board)

    if square is not None:
        for num in range(1, 10):
            if is_num_ok_in_square(num, square["row"], square["col"], board):
                board[square["row"]][square["col"]] = num

                if sudoku(board):
                    return True
                else:
                    board[square["row"]][square["col"]] = EMPTY
        return False
    return True
