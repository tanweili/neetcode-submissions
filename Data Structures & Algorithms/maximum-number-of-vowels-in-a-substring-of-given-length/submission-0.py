class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ('a','e','i','o','u')
        current_window_vowels = 0
        current_window = s[:k]
        for ltr in current_window:
            if ltr in vowels:
                current_window_vowels += 1
        ans = current_window_vowels
        left, right = 0, k
        while right < len(s):
            if s[left] in vowels:
                current_window_vowels -= 1
            if s[right] in vowels:
                current_window_vowels += 1
            ans = max(ans, current_window_vowels)
            left += 1
            right += 1
        return ans
