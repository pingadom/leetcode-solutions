class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = {}

        for x in nums:
            # Option 1: Increment x to x + 1
            dp[x + 1] = max(dp.get(x + 1, 0), dp.get(x, 0) + 1)

            # Option 2: Keep x unchanged
            dp[x] = max(dp.get(x, 0), dp.get(x - 1, 0) + 1)

        return max(dp.values())