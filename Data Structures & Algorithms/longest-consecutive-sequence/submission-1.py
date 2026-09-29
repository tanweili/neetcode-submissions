class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        output = 0
        while len(s) != 0:
            left = s.pop()
            right = left
            while left - 1 in s:
                s.remove(left - 1)
                left -= 1
            while right + 1 in s:
                s.remove(right + 1)
                right += 1
            output = max(output, right - left + 1)
        return output

