class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row_counts = [None for _ in range(len(grid))]
        col_counts = [None for _ in range(len(grid[0]))]
        for i in range(len(grid)):
            row_counts[i] = sum(grid[i])
        for j in range(len(grid[0])):
            current_count = 0
            for k in range(len(grid)):
                current_count += grid[k][j]
            col_counts[j] = current_count
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and row_counts[row] > 1:
                    ans += 1
                elif grid[row][col] == 1 and col_counts[col] > 1:
                    ans += 1
        return ans