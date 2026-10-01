class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1. Find index of largest element
        left, right = 0, len(nums) - 1
        while left < right:
            mid = right - (right - left) // 2
            if nums[mid] > nums[left]:
                left = mid
            else:
                right = mid - 1
        largest_element_idx = left
        # 2. Set correct bounds to search for target
        if largest_element_idx == len(nums):
            left, right = 0, len(nums) - 1
        elif nums[0] <= target and target <= nums[largest_element_idx]:
            left, right = 0, largest_element_idx
        else:
            left, right = largest_element_idx + 1, len(nums) - 1
        # print(f"left {left} right {right}")
        # 3. Search for target
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid
                break
            if nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        # print(f"left {left} right {right}")
        return left if left < len(nums) and nums[left] == target else -1

        