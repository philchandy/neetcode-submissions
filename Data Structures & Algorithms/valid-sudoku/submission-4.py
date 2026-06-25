class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        squares = defaultdict(set)
        rows = defaultdict(set)
        cols = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                val = board[i][j]

                box = (i//3, j//3)

                if val == ".":
                    continue
                if (val in cols[j] or 
                    val in rows[i] or 
                    val in squares[box]):
                    return False
                cols[j].add(val)
                rows[i].add(val)
                squares[box].add(val)
        
        return True
        
        