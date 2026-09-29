class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = dict()
        for n in nums:
            if n in hm.keys():
                hm[n] += 1
            else:
                hm[n] = 1
        lst = []
        for _key, _value in hm.items():
            heapq.heappush(lst, (_value, _key))
            if len(lst) > k:
                heapq.heappop(lst)
        return [_k for _v, _k in lst]

        
            