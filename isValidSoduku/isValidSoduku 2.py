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
        N = 9
        gridSets = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                gridId = (r // 3) * 3 + (c // 3)

                cell = board[r][c]
                if cell == self.empty_field:
                    continue

                if cell in gridSets[gridId]:
                    return False

                gridSets[gridId].add(cell)

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return (
            self.hasValidRows(board)
            and self.hasValidColumns(board)
            and self.hasValidSquares(board)
        )
