class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = []
        for i in range(len(nums1)):
            nums.append((nums1[i], nums2[i]))
        nums.sort(key=lambda x: (x[1], x[0]), reverse = True)
        current_sum = 0
        current_sum_list = []
        ans = 0
        for i in range(len(nums)):
            current_sum += nums[i][0]
            heapq.heappush(current_sum_list, nums[i][0])
            if len(current_sum_list) == k:
                ans = max(ans, current_sum * nums[i][1])
                current_sum -= heapq.heappop(current_sum_list)
        return ans


