class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lst = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i-1] == nums[i]:
                continue # If the element i-1 is the same as i, I have already processed a case where i of i,j,k is this value
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    lst.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
        return lst
