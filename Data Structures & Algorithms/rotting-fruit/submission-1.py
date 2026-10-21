class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        dq = deque()
        minutes = 0
        dir = [-1,0,1,0,-1]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    dq.append((i,j))
        if len(dq) == 0 and fresh == 0:
            return 0
        while len(dq) != 0:
            current_length = len(dq)
            minutes += 1
            while current_length != 0:
                current_length -= 1
                current_row, current_col = dq.popleft()
                for i in range(4):
                    if current_row + dir[i] >= 0 and current_row + dir[i] < len(grid)\
                    and current_col + dir[i+1] >= 0 and current_col + dir[i+1] < len(grid[0])\
                    and grid[current_row + dir[i]][current_col + dir[i+1]] == 1:
                        grid[current_row + dir[i]][current_col + dir[i+1]] = 2
                        fresh -= 1
                        dq.append((current_row + dir[i], current_col + dir[i+1]))
        if fresh == 0:
            return minutes - 1
        else:
            return -1