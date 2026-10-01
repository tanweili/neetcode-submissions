class Solution:
    output = []
    nums = []
    def backtrack(self, idx: int, current_list: List[int]) -> None:
        if idx == len(self.nums):
            self.output.append(current_list.copy())
            return
        current_list.append(self.nums[idx])
        self.backtrack(idx + 1, current_list)
        current_list.pop()
        self.backtrack(idx + 1, current_list)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.output = []
        self.nums = nums
        self.backtrack(0, [])
        return self.output