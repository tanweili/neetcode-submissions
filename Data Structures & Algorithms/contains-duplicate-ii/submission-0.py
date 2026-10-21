class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm = {}
        for i in range(len(nums)):
            if nums[i] not in hm.keys():
                hm[nums[i]] = [i]
                continue
            for idx in hm[nums[i]]:
                if abs(idx - i) <= k:
                    return True
            hm[nums[i]].append(i)
        return False