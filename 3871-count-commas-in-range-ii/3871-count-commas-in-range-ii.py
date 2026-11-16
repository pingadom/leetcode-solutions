class Solution:
    def countCommas(self, n: int) -> int:
        big,small = 10**3,1
        res = 0

        while n > big-1:
            big *= 10**3
            small *= 10**3

        
        while small > 999:
            n_c = int(round(math.log(small,10)))//3
            print(int(small-1))
            n_above = int(n - small +1)
            print(n_above,n,small)
            res += n_c * n_above
            print(res)
            n = small -1
            small /= 10**3
        return res
        

        
