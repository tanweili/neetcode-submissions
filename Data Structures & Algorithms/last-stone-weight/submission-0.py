class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            heavier = heapq.heappop_max(stones)
            lighter = heapq.heappop_max(stones)
            if heavier == lighter:
                continue
            else:
                heapq.heappush_max(stones, heavier - lighter)
        if len(stones) == 1:
            return stones[0]
        else:
            return 0