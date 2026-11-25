class Solution:
    def totalNQueens(self, n: int) -> list[list[str]]:
        result = 0
        cols = set()
        pos_diag = set()
        neg_diag = set()
        board = [["."] * n for _ in range(n)]

        def backtrack(row):
            nonlocal result

            if row == n:

                result += 1
                return

            for col in range(n):
                if (col in cols or
                    row + col in pos_diag or
                    row - col in neg_diag):
                    continue

                board[row][col] = "Q"
                cols.add(col)
                pos_diag.add(row+col)
                neg_diag.add(row-col)

                backtrack(row+1)

                board[row][col] = "."
                cols.remove(col)
                pos_diag.remove(row+col)
                neg_diag.remove(row-col)

        backtrack(0)
        return result   