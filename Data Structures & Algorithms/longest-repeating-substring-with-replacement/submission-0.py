class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ltr_cnts = [0 for _ in range(26)]
        left, right, output = 0, 0, 0
        while right < len(s):
            ltr_cnts[ord(s[right]) - ord('A')] += 1
            # sum(ltr_cnts) - max(ltr_cnts) is the number of replacments needed
            if sum(ltr_cnts) - max(ltr_cnts) <= k:
                output = max(output, (right - left + 1))
            else:
                while left < right and sum(ltr_cnts) - max(ltr_cnts) > k:
                    ltr_cnts[ord(s[left]) - ord('A')] -= 1
                    left += 1
            right += 1
        return output