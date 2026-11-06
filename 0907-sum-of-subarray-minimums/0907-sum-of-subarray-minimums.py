class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        result = 0
        n = len(arr)

        for i in range(n + 1):
            while stack and (i == n or arr[stack[-1]] >= arr[i]):
                j = stack.pop()

                left = j - stack[-1] if stack else j + 1
                right = i - j

                result += arr[j] * left * right

            stack.append(i)

        return result % MOD