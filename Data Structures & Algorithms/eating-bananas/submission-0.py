class Solution:
    def calcHoursNeeded(self, piles: List[int], eating_spd: int) -> int:
        output = 0
        for pile in piles:
            output += pile // eating_spd
            if pile % eating_spd > 0:
                output += 1
        # print(f"eating speed {eating_spd} hours needed {output}")
        return output

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles) # left and right represent the minimum and maximum eating rate
        while left < right:
            mid = left + (right - left) // 2
            if self.calcHoursNeeded(piles, mid) > h:
                left = mid + 1
            else:
                right = mid
        return left