class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 1
        left, right = 0, 0
        current_window_total = 0
        while right < len(nums):
            target_num = nums[right]
            current_window_total += nums[right]
            if current_window_total + k >= (right - left + 1) * target_num:
                ans = max(ans, (right - left + 1))
            else:
                while left < right and current_window_total + k < (right - left + 1) * target_num:
                    current_window_total -= nums[left]
                    left += 1
            right += 1
        return ans

