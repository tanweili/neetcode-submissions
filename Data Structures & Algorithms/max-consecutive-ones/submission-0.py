class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ln = 0
        current_ln = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                current_ln += 1
            else:
                current_ln = 0
            max_ln = max(max_ln, current_ln)
        return max_ln
        