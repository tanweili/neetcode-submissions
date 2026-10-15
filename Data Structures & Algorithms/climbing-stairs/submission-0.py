class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp_1d = [0 for _ in range(n)]
        dp_1d[0], dp_1d[1] = 1, 2
        for i in range(2, n):
            dp_1d[i] = dp_1d[i-1] + dp_1d[i-2]
        return dp_1d[-1]
