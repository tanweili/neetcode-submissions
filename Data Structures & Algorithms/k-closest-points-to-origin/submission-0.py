class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [(p[0] ** 2 + p[1] ** 2,p[0],p[1]) for p in points]
        ans = []
        heapq.heapify(points)
        while k > 0:
            k -= 1
            current_point = heapq.heappop(points)
            ans.append((current_point[1], current_point[2]))
        return ans