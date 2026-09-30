class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1: Find the greatest 0-idx row value that is <= target
        left, right = 0, len(matrix) - 1
        while left < right:
            mid = right - (right - left) // 2 # Left bias version to get greatest value that is <= target
            if matrix[mid][0] > target:
                right = mid - 1 # Paired with mid - 1 to avoid infinite loop
            else:
                left = mid
        # 2: Within the row, check for the target value
        target_row = left
        left, right = 0, len(matrix[0]) - 1
        while left < right:
            mid = left + (right - left) // 2
            if matrix[target_row][mid] == target:
                return True
            elif matrix[target_row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if matrix[target_row][left] == target:
            return True
        else:
            return False

