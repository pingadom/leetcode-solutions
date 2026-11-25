class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n // 2):
            for j in range(i, n - i - 1):
                temp = matrix[i][j]

                # Top <- Left
                matrix[i][j] = matrix[n-1-j][i]

                # Left <- Bottom
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]

                # Bottom <- Right
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]

                # Right <- Top
                matrix[j][n-1-i] = temp