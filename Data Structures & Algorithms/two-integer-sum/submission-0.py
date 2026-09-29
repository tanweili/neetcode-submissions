class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hs = dict()
        for i in range(len(nums)):
            if target - nums[i] in hs.keys():
                return [hs[target - nums[i]], i]
            hs[nums[i]] = i
        return [-1]
        