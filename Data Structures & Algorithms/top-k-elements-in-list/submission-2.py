class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = dict()
        for n in nums:
            if n in hm.keys():
                hm[n] += 1
            else:
                hm[n] = 1
        freq_map = [[] for _ in range(len(nums)+1)]
        for num, cnt in hm.items():
            freq_map[cnt].append(num)
        output = []
        for i in range(len(freq_map) - 1, 0, -1):
            for num in freq_map[i]:
                output.append(num)
                if len(output) == k:
                    return output

        
            