class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        squares = {}

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                value = board[i][j]

                if value in row[i]:
                    return False
                if value in col[j]:
                    return False
                
                square = (i//3, j//3)
                if square not in squares:
                    squares[square] = set()
                if value in squares[square]:
                    return False

                row[i].add(value)
                col[j].add(value)
                squares[square].add(value)
        
        return True



                
        
