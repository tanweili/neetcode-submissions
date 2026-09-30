class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, max_ln = 0, 0, 0
        hs = set()
        while right < len(s):
            if s[right] not in hs:
                hs.add(s[right])
                max_ln = max(max_ln, (right - left + 1))
            else:
                while left < right and s[right] in hs:
                    hs.remove(s[left])
                    left += 1
                hs.add(s[right])
            right += 1
        return max_ln
