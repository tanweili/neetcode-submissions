class Solution:
    ans = []
    visited = set()
    nums = []
    def dfs(self, current_list: List[int]):
        if len(current_list) == len(self.nums):
            self.ans.append(current_list.copy())
            return
        for i in range(0, len(self.nums)):
            if i in self.visited:
                continue
            current_list.append(self.nums[i])
            self.visited.add(i)
            self.dfs(current_list)
            self.visited.remove(i)
            current_list.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.visited = set()
        self.nums = nums
        self.dfs([])
        return self.ans