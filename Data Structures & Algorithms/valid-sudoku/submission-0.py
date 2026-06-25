class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        squares = defaultdict(set)

        for i in range(len(board)):
            rows = set()
            for j in range(len(board[0])):
                if board[i][j] == ".": 
                    continue
                if board[i][j] in rows:
                    return False
                
                rows.add(board[i][j])
        
        for i in range(len(board)):
            cols = set()
            for j in range(len(board[0])):
                if board[j][i] == ".":
                    continue
                if board[j][i] in cols:
                    return False
                cols.add(board[j][i])
        
        for i in range(len(board)):
            for j in range(len(board[0])):

                box = (i//3, j//3)
                if board[i][j] == ".":
                    continue
                if board[i][j] in squares[box]:
                    return False
                
                squares[box].add(board[i][j])
        return True
        
        