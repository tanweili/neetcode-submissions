import heapq
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        ls = []
        for i in range(len(nums)):
            ls.append((len(nums[i]), nums[i]))
        heapq.heapify_max(ls)
        while k > 1:
            k -= 1
            heapq.heappop_max(ls)
        return ls[0][1]
