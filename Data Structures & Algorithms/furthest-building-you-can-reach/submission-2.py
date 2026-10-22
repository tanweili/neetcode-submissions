class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        current_cost = 0
        cost_array = [0]
        ans = 0
        for i in range(1, len(heights)):
            if heights[i] > heights[i-1]:
                current_cost += heights[i] - heights[i-1]
                heapq.heappush_max(cost_array, heights[i] - heights[i-1])
            if current_cost <= bricks:
                ans = i
            elif ladders > 0:
                while ladders > 0 and current_cost > bricks and len(cost_array) > 0:
                    current_cost -= heapq.heappop_max(cost_array)
                    ladders -= 1
                ans = i
            else:
                break
        return ans
            

