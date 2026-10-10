class Solution:
    def minOperations(self, nums: List[int]) -> int:
        hm = {}
        for n in nums:
            if n not in hm.keys():
                hm[n] = 1
            else:
                hm[n] += 1
        ans = 0
        for _, v in hm.items():
            if v == 1:
                ans = -1
                break
            if v % 3 == 0:
                ans += v // 3
            elif v % 3 == 2:
                ans += (v // 3) + 1
            elif v % 3 == 1:
                ans += (v // 3) + 1
            elif v % 2 == 0:
                ans += v // 2
            elif v % 2 == 1:
                ans += (v - 1) // 2
        
        return ans