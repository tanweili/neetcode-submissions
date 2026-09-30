class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_letter_cnts = [0 for _ in range(26)]
        for ltr in s1:
            s1_letter_cnts[ord(ltr) - ord('a')] += 1
        s2_letter_cnts = [0 for _ in range(26)]
        for i in range(len(s1)):
            s2_letter_cnts[ord(s2[i]) - ord('a')] += 1
        left, right = 0, len(s1)
        while right < len(s2):
            if s1_letter_cnts == s2_letter_cnts:
                return True
            else:
                s2_letter_cnts[ord(s2[right]) - ord('a')] += 1
                s2_letter_cnts[ord(s2[left]) - ord('a')] -= 1
            right += 1
            left += 1
        if s1_letter_cnts == s2_letter_cnts:
            return True
        else:
            return False