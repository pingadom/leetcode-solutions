class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        p1,p2 = 0,len(needle)
        for n in range(p2-1,len(haystack)):
            if haystack[p1:p2] == needle:
                return p1
            else:
                p1+=1
                p2+=1
        return -1