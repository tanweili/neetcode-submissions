class Solution:
    lst = [-1,0,1,0,-1]
    def dfs(self, row: int, col: int, board: List[List[str]]) -> None:
        board[row][col] = '#'
        for i in range(4):
            if row + self.lst[i] >= 0 and row + self.lst[i] < len(board)\
            and col + self.lst[i+1] >= 0 and col + self.lst[i+1] < len(board[0])\
            and board[row + self.lst[i]][col + self.lst[i+1]] == 'O':
                self.dfs(row + self.lst[i], col + self.lst[i+1], board)

    def solve(self, board: List[List[str]]) -> None:
        for i in range(len(board)):
            if board[i][0] == 'O':
                self.dfs(i,0,board)
            if board[i][-1] == 'O':
                self.dfs(i,len(board[0]) - 1,board)
        
        for j in range(len(board[0])):
            if board[0][j] == 'O':
                self.dfs(0,j,board)
            if board[-1][j] == 'O':
                self.dfs(len(board)-1,j,board)
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '#':
                    board[row][col] = 'O'
                elif board[row][col] == 'O':
                    board[row][col] = 'X'