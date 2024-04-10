from typing import List
import numpy as np


class Solution:
    empty_field = "."

    def isUniqueList(self, data_list: List[str]) -> bool:
        occurences = {}
        for item in data_list:
            occurences[item] = occurences.get(item, 0) + 1
            if occurences[item] > 1 and item != self.empty_field:
                return False
        # print(occurences)
        return True

    def hasValidRows(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.isUniqueList(row):
                return False
        return True

    def hasValidColumns(self, board: List[List[str]]) -> bool:
        # normal board list is a row-by-row list, board_transposed is a column-by-column list
        board_transposed = np.array(board).T
        for column in board_transposed:
            if not self.isUniqueList(list(column)):
                return False
        return True

    def hasValidSquares(self, board: List[List[str]]) -> bool:
        # This method is valid only for 9 x 9 Soduku
        square_row_iterator = 0
        square_col_iterator = 0

        checked_squares = 0
        while checked_squares <= 9:
            square_details = {}
            for r in range(3):
                for c in range(3):
                    row = r + (square_row_iterator * 3)
                    col = c + (square_col_iterator * 3)
                    cell = board[row][col]
                    square_details[cell] = square_details.get(cell, 0) + 1
                    if (
                        square_details[cell] > 1
                        and cell != self.empty_field
                    ):
                        return False
            checked_squares += 1
            square_row_iterator = (square_row_iterator + 1) % 3
            if square_row_iterator == 0:
                square_col_iterator = (square_col_iterator + 1) % 3

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (
            self.hasValidRows(board)
            and self.hasValidColumns(board)
            and self.hasValidSquares(board)
        )