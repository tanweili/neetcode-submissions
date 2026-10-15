class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        already_not_grumpy = 0
        max_can_be_not_grumpy = 0
        current_can_be_not_grumpy = 0
        for i in range(minutes):
            if grumpy[i] == 0:
                already_not_grumpy += customers[i]
            else:
                current_can_be_not_grumpy += customers[i]
        max_can_be_not_grumpy = max(max_can_be_not_grumpy, current_can_be_not_grumpy)
        left, right = 0, minutes
        while right < len(customers):
            if grumpy[left] == 1:
                current_can_be_not_grumpy -= customers[left]
            if grumpy[right] == 0:
                already_not_grumpy += customers[right]
            else:
                current_can_be_not_grumpy += customers[right]
            max_can_be_not_grumpy = max(max_can_be_not_grumpy, current_can_be_not_grumpy)
            left += 1
            right += 1
        return already_not_grumpy + max_can_be_not_grumpy
        