class Solution:
    def countAndSay(self, n: int) -> str:
        def rec(n):
            if n == 1:
                return "1"
            else:
                p = rec(n-1)

            final = ""
            p = str(p)
            if len(p) > 1:
                curr = p[0]
            else:
                curr = p
            prev = 0
            for i in range(1,len(p)):
                if p[i] != curr:
                    final = final + str(i-prev) + curr
                    curr = p[i]
                    prev = i
            final = final + str(len(p)-prev) + curr
            return final

        return rec(n)
