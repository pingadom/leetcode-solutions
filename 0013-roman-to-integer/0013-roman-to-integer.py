class Solution:
    def romanToInt(self, s: str) -> int:
        num = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        final = 0
        n = 0

        while n <= len(s)-1:

            if (s[n:n+2] in num):
                final += num[s[n:n+2]]
                n+=2
            else:
                final += num[s[n]]
                n+=1

        return final



        