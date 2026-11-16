class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:

        def candidates(r, c):
            possible = set("123456789")

            possible -= set(board[r])
            possible -= {board[i][c] for i in range(9)}

            br = (r // 3) * 3
            bc = (c // 3) * 3

            for i in range(br, br + 3):
                for j in range(bc, bc + 3):
                    possible.discard(board[i][j])

            return possible

        def solve():
            best = None
            best_candidates = None

            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        options = candidates(r, c)

                        if not options:
                            return False

                        if (best_candidates is None or
                            len(options) < len(best_candidates)):

                            best = (r, c)
                            best_candidates = options

                            if len(options) == 1:
                                break

                if best_candidates is not None and len(best_candidates) == 1:
                    break

            if best is None:
                return True

            r, c = best

            for num in best_candidates:
                board[r][c] = num

                if solve():
                    return True

                board[r][c] = "."

            return False

        solve()