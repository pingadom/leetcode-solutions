
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        # STEP 1: Precompute substring costs
        cost = [[float("inf")] * (n + 1) for _ in range(n)]

        for i in range(n):
            for j in range(i + 2, n + 1):
                length = j - i

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0
                    group_len = length // d

                    for r in range(d):
                        for t in range(group_len // 2):
                            left = i + r + t * d
                            right = i + r + (group_len - 1 - t) * d

                            if s[left] != s[right]:
                                changes += 1

                    cost[i][j] = min(cost[i][j], changes)

        # STEP 2: Dynamic programming
        INF = float("inf")
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for t in range(1, k + 1):
            for i in range(2 * t, n + 1):

                # Try every possible start of the last substring
                for j in range(2 * (t - 1), i - 1):
                    dp[t][i] = min(
                        dp[t][i],
                        dp[t - 1][j] + cost[j][i]
                    )

        return dp[k][n]
