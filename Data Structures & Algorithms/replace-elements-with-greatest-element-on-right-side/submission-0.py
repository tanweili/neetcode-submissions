class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = None
        for i in range(len(arr) - 1, -1, -1):
            if greatest is None:
                greatest = arr[i]
                arr[i] = -1
            else:
                original_val = arr[i]
                arr[i] = greatest
                greatest = max(greatest, original_val)
        return arr