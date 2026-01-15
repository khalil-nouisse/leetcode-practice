"""
Valid Sudoku
============

Problem:
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated.

Idea:
Use Hash Sets to track seen numbers for each row, column, and 3x3 square.
- `rows[r]` stores numbers seen in row `r`.
- `cols[c]` stores numbers seen in column `c`.
- `squares[(r//3, c//3)]` stores numbers seen in the 3x3 sub-grid at coordinates (r//3, c//3).

Complexity:
- Time: O(9^2) = O(1) since the board size is fixed.
- Space: O(9^2) = O(1) to store the sets.
"""

from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Validates a Sudoku board.
        """
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  # Key: (row // 3, col // 3)

        for r in range(9):
            for c in range(9):
                cell_value = board[r][c]
                
                # Skip empty cells
                if cell_value == ".":
                    continue
                
                # Check if value already exists in current row, col, or square
                if (cell_value in rows[r] or
                    cell_value in cols[c] or
                    cell_value in squares[(r // 3, c // 3)]):
                    return False

                # Add value to trackers
                cols[c].add(cell_value)
                rows[r].add(cell_value)
                squares[(r // 3, c // 3)].add(cell_value)

        return True

if __name__ == "__main__":
    solution = Solution()
    
    board = [
        ["1", "2", ".", ".", "3", ".", ".", ".", "."],
        ["4", ".", ".", "5", ".", ".", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", ".", "3"],
        ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
        [".", ".", ".", "8", ".", "3", ".", ".", "5"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", ".", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "8"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    
    print("Board:")
    for row in board:
        print(row)
        
    print(f"\nIs Valid Sudoku: {solution.isValidSudoku(board)}")