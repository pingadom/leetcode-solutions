from bisect import bisect_left,bisect_right

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row = bisect_right(matrix, target, key=lambda r: r[0]) - 1
        if row < 0:
            return False
        
        col = bisect_left(matrix[row],target)
    
        return col < len(matrix[row]) and matrix[row][col] == target