class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_bucket = [0 for _ in range(26)]
        t_bucket = [0 for _ in range(26)]
        for letter in s:
            s_bucket[ord(letter) - ord('a')] += 1
        for letter in t:
            t_bucket[ord(letter) - ord('a')] += 1
        for i in range(26):
            if s_bucket[i] != t_bucket[i]:
                return False
        return True        