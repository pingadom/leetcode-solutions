class Solution:
    def reverse(self, x: int) -> int:

        neg = 1
        if x < 0:
            neg = -1
            x = x*-1
        
        x = neg*int(str(x)[::-1])
        if (x >= -(2**31)) and (x <= (2**31)-1):
            return x
        else:
            return 0

        