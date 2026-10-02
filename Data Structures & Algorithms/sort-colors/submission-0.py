class Solution:
    def sortColors(self, nums: List[int]) -> None:
        ptr0, ptr1, ptr2 = 0,0,len(nums) - 1
        while ptr1 <= ptr2:
            if nums[ptr1] == 0:
                nums[ptr0], nums[ptr1] = nums[ptr1], nums[ptr0]
                ptr0 += 1
                ptr1 += 1
            elif nums[ptr1] == 1:
                ptr1 += 1
            else:
                nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
                ptr2 -= 1
        

        