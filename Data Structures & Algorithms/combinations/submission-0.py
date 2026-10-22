class Solution:
    ans = []
    k = 0
    n = 0

    def dfs(self, idx: int, current_list: List[int]):
        if len(current_list) == self.k:
            self.ans.append(current_list.copy())
            return
        for i in range(idx, self.n + 1):
            current_list.append(i)
            self.dfs(i + 1, current_list)
            current_list.pop()
            

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        self.k = k
        self.n = n
        self.dfs(1, [])
        return self.ans
