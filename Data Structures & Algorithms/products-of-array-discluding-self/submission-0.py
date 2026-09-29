class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_sum = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i-1] * nums[i-1]
        suffix_sum = [1 for _ in range(len(nums))]
        for i in range(len(nums)-2,-1,-1):
            suffix_sum[i] = suffix_sum[i+1] * nums[i+1]
        output = []
        for i in range(len(nums)):
            output.append(prefix_sum[i] * suffix_sum[i])
        return output
        