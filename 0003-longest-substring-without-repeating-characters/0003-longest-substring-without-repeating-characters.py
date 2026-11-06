class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        m = 0
        for n in range(0,len(s)):
            if s[n] not in seen:
                seen.append(s[n])
            else:
                seen = seen[seen.index(s[n])+1:]
                seen.append(s[n])
            
            if len(seen) > m:
                m = len(seen)      
        
        return m
        