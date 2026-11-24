class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        l = len(nums)
        res = []

        def dp(a,m_a):
            if len(a) == 0:
                res.append(m_a)
                return
            for n in range(len(a)):
                t = set(a)
                t.remove(a[n])
                dp(list(t),m_a + [a[n]])
        
        dp(nums,[])
        return res


