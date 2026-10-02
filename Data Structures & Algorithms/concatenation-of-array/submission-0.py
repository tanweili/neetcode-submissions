class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ln_nums = len(nums)
        for i in range(ln_nums):
            nums.append(nums[i])
        return nums