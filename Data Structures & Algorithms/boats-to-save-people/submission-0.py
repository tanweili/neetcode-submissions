class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        left, right = 0, len(people) - 1
        while left <= right:
            if left == right:
                boats += 1
                break
            remaining_limit = limit - people[right]
            right -= 1
            if left <= right and people[left] <= remaining_limit:
                left += 1
            boats += 1
        return boats