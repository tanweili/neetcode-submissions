class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        window = deque()
        for i in range(k):
            window.append(nums[i])
        ans = window[-1] - window[0]
        right = k
        while right < len(nums):
            window.popleft()
            window.append(nums[right])
            ans = min(ans, window[-1] - window[0])
            right += 1
        return ans