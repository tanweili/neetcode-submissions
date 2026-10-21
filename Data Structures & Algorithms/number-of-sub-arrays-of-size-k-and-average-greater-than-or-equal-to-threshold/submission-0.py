class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        current_window_sum = 0
        for i in range(k):
            current_window_sum += arr[i]
        if current_window_sum / k >= threshold:
            ans += 1
        left, right = 0, k
        while right < len(arr):
            current_window_sum -= arr[left]
            current_window_sum += arr[right]
            if current_window_sum / k >= threshold:
                ans += 1
            left += 1
            right += 1
        return ans