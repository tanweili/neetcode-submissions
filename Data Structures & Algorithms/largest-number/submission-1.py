from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(lambda x: str(x), nums))
        def cmp(a: str, b: str) -> int:
            ab = a + b
            ba = b + a
            if ab > ba:
                return - 1
            elif ab < ba:
                return 1
            else:
                return 0
        nums.sort(key=cmp_to_key(cmp))
        return str(int(''.join(nums)))