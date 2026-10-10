class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return False
        hm = set()
        hm.add(0)
        current_sum = 0
        for i in range(len(nums) - 1):
            current_sum_window = current_sum + nums[i] + nums[i + 1] # Need this to ensure at least subarray of size two
            hm.add(current_sum % k)
            target_to_find = (current_sum_window % k)
            if target_to_find in hm:
                return True
            else:
                hm.add(current_sum)
                current_sum += nums[i]
        return False