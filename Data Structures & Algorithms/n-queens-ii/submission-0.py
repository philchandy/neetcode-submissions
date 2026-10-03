class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [['.'] * n for _ in range(n)]
        solutions = []

        visited_cols = set()
        visited_diags = set()
        visited_d2 = set()

        def isValid(row, col):
            if col in visited_cols:
                return False
            elif row - col in visited_diags:
                return False
            elif row + col in visited_d2:
                return False
            return True
        
        def dfs(row):
            if n == row:
                cp = ["".join(row) for row in board]
                solutions.append(cp)
                return
            for col in range(n):
                if isValid(row, col):
                    board[row][col] = 'Q'
                    visited_cols.add(col)
                    visited_diags.add(row-col)
                    visited_d2.add(row+col)

                    dfs(row+1)
                    
                    board[row][col] = '.'
                    visited_cols.remove(col)
                    visited_diags.remove(row-col)
                    visited_d2.remove(row+col)
        dfs(0)
        return len(solutions)


        # dfs solution



        # check col, row
        # 
        
        