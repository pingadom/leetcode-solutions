from functools import cache
from typing import List

class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:

        @cache
        def dp(step_at):
            if step_at == n:
                return 0

            opts = []
            c = step_at

            while c < n and c < step_at + 3:
                c += 1

                jump_cost = (c - step_at) ** 2
                step_cost = costs[c - 1]

                opts.append(
                    jump_cost + step_cost + dp(c)
                )

            return min(opts)

        return dp(0)