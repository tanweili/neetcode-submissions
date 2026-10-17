class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hm = {}
        for n in arr:
            if n not in hm.keys():
                hm[n] = 1
            else:
                hm[n] += 1
        hm = [(v,k) for k,v in hm.items()]
        heapq.heapify(hm)
        while len(hm) > 0 and k > 0:
            if k - hm[0][0] >= 0:
                k -= hm[0][0]
                heapq.heappop(hm)
            else:
                break
        return len(hm)
