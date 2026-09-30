class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = right - (right - left) // 2
            if nums[mid] < nums[left]:
                right = mid - 1
            else:
                left = mid
        if left != len(nums) - 1:
            return nums[left + 1]
        else:
            return nums[0]

# n+1 ... max | min ... ... ... ... ... ... ... ... n 