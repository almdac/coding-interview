#https://leetcode.com/explore/item/2804

class Solution:        
    def _valid(self, candidate_column: int, board: list[int]) -> bool:
        candidate_row = board[candidate_column]
        for column, row in enumerate(board[:candidate_column]):
            if candidate_row == row:
                return False
            elif candidate_row-candidate_column == row-column:
                return False
            elif candidate_row+candidate_column == row+column:
                return False
        return True
    
    def backtrack(self, n: int, column: int, board: list[int]) -> int:
        solutions = 0
        board[column] = 0
        while board[column] < n:
            valid = self._valid(column, board)
            if valid and column == n-1:
                solutions += 1
            elif valid and column < n-1:
                solutions += self.backtrack(n, column+1, board)
            board[column] += 1
        return solutions
        
    def totalNQueens(self, n: int) -> int:
        return self.backtrack(n, 0, [0]*n)