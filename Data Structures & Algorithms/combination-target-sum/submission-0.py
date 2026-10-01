class Solution:
    output = []
    target = 0
    nums = []

    def dfs(self, idx: int, current_list: List[int]) -> None:
        if sum(current_list) == self.target:
            self.output.append(current_list.copy())
            return
        elif sum(current_list) > self.target:
            return
        for i in range(idx, len(self.nums)):
            current_list.append(self.nums[i])
            self.dfs(i,current_list)
            current_list.pop()

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.output = []
        self.target = target
        self.nums = nums
        self.dfs(0, [])
        return self.output