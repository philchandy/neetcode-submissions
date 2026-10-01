class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diags = set()
        diags2 = set()

        solutions = []
        board = [['.'] * n for _ in range(n)]

        def isValid(row, col):
            diag = row - col
            diag2 = row + col
            if (col in cols) or (diag in diags) or (diag2 in diags2):
                return False
            return True
        
        def dfs(row):
            if n == row:
                cp = ["".join(row) for row in board]
                solutions.append(cp)
                return 
            for col in range(n):
                if isValid(row, col):
                    cols.add(col)
                    diags.add(row - col)
                    diags2.add(row + col)

                    board[row][col] = 'Q'

                    dfs(row+1)

                    board[row][col] = '.'

                    cols.remove(col)
                    diags.remove(row - col)
                    diags2.remove(row + col)
        dfs(0)
        return solutions