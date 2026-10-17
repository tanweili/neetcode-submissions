class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        lst = [-1,0,1,0,-1]
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    ans += 1
                    q = deque()
                    q.append((row,col))
                    grid[row][col] = '0'
                    while len(q) != 0:
                        current_row, current_col = q.popleft()
                        for i in range(4):
                            if (current_row + lst[i]) >= 0 and (current_row + lst[i]) < len(grid) \
                            and (current_col + lst[i+1]) >= 0 and (current_col + lst[i+1]) < len(grid[0]) \
                            and grid[current_row + lst[i]][current_col + lst[i+1]] == '1':
                                grid[current_row + lst[i]][current_col + lst[i+1]] = '0'
                                q.append((current_row + lst[i], current_col + lst[i+1]))
        return ans