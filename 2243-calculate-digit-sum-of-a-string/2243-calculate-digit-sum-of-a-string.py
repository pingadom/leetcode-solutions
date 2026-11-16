class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            chunks = [s[i:i+k] for i in range (0,len(s),k)]
            s = ""
            for c in chunks:
                c = list(map(int,c))
                s = s + str(sum(c))

        return s