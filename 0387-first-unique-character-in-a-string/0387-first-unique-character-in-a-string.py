from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for i in range(0,len(s)):
            if c[s[i]] == 1:
                return i
        return -1
        