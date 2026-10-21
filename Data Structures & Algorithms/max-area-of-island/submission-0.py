class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        lst = [-1,0,1,0,-1]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area = 1
                    dq = deque()
                    dq.append((row,col))
                    grid[row][col] = 0
                    while len(dq) != 0:
                        current_row, current_col = dq.popleft()
                        for i in range(4):
                            if current_row + lst[i] >= 0 and current_row + lst[i] < len(grid)\
                            and current_col + lst[i+1] >= 0 and current_col + lst[i+1] < len(grid[0])\
                            and grid[current_row + lst[i]][current_col + lst[i+1]] == 1:
                                grid[current_row + lst[i]][current_col + lst[i+1]] = 0
                                area += 1
                                dq.append((current_row + lst[i], current_col + lst[i+1]))
                    ans = max(ans, area)
        return ans