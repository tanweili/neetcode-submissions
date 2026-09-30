class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([letter.lower() for letter in s if letter.isalnum()])
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
        