class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in range(len(board)):
            s = set()
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    continue
                if board[row][col] in s:
                    return False
                else:
                    s.add(board[row][col])
        # Check columns
        for col in range(len(board[0])):
            s = set()
            for row in range(len(board)):
                if board[row][col] == ".":
                    continue
                if board[row][col] in s:
                    return False
                else:
                    s.add(board[row][col])

        # Check 3x3 squares
        for i in range(9):
            s = set()
            r, c = (i % 3) * 3, (i // 3) * 3
            for u in range(3):
                for v in range(3):
                    if board[r+u][c+v] == ".":
                        continue
                    if board[r+u][c+v] in s:
                        return False
                    else:
                        s.add(board[r+u][c+v])
        return True
        