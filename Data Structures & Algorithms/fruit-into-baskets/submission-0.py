class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        b1_value, b2_value = None, None
        b1_count, b2_count = 0, 0
        left, right = 0, 0
        ans = 1
        while right < len(fruits):
            if b1_value is None:
                b1_value = fruits[right]
                b1_count += 1
            elif b2_value is None:
                b2_value = fruits[right]
                b2_count += 1
            elif fruits[right] == b1_value:
                b1_count += 1
            elif fruits[right] == b2_value:
                b2_count += 1
            else:
                while left < right and b1_count > 0 and b2_count > 0:
                    if fruits[left] == b1_value:
                        b1_count -= 1
                    elif fruits[left] == b2_value:
                        b2_count -= 1
                    left += 1
                if b1_count == 0:
                    b1_value = fruits[right]
                    b1_count += 1
                elif b2_count == 0:
                    b2_value = fruits[right]
                    b2_count += 1
            ans = max(ans, right - left + 1)        
            right += 1
        return ans