class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        back_ptr = m + n - 1
        it1, it2 = m - 1, n - 1
        while it1 >= 0 or it2 >= 0:
            if it1 < 0:
                nums1[back_ptr] = nums2[it2]
                back_ptr -= 1
                it2 -= 1
            elif it2 < 0:
                break 
            elif nums1[it1] >= nums2[it2]:
                nums1[back_ptr] = nums1[it1]
                it1 -= 1
                back_ptr -= 1
            elif nums2[it2] > nums1[it1]:
                nums1[back_ptr] = nums2[it2]
                it2 -= 1
                back_ptr -= 1



