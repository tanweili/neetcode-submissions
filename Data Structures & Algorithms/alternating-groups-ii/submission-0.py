class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        ans = 0
        left = 0
        for right in range(1, len(colors) + k - 1):
            if colors[right % len(colors)] == colors[(right - 1) % len(colors)]:
                left = right
            if right - left + 1 > k:
                left += 1
            if right - left + 1 == k:
                ans += 1
        return ans
