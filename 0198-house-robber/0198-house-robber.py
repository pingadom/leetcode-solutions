class Solution:
    def rob(self, nums: list[int]) -> int:

        @cache
        def dp(a,s):
            l = len(a)
            a = list(a)
            if l == 0:
                return 0
            if l == 1:
                return a[0]
            if l == 2:
                return max(a[0],a[1])
            if l == 3:
                return max(a[0] + a[2],a[1])
            if s == 1:
                return (a[0]+dp(tuple(a[2:]),0))
            return max((a[0]+dp(tuple(a[2:]),0)),dp(tuple(a[1:]),1))
        nums = tuple(nums)
        return dp((nums),0)