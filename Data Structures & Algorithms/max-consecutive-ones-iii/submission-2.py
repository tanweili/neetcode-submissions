class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if k == 0:
            return sum(nums)
        ans = 0
        left, right = 0, 0
        zero_cnt = 0
        ans = 0
        while right < len(nums):
            if nums[right] == 0:
                if zero_cnt < k:
                    zero_cnt += 1
                else:
                    while left < right and not zero_cnt < k:
                        if nums[left] == 0:
                            zero_cnt -= 1
                        left += 1
                    zero_cnt += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans
