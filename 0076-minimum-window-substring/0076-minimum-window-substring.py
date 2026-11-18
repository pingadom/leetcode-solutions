from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        need = Counter(t)
        window = {}
        formed = 0
        best = ""
        len_best = float("inf")

        for right, char in enumerate(s):
            if char in need:
                window[char] = window.get(char,0) + 1
            else:
                continue
            if window[char] == need[char]:
                formed += 1

            while formed == len(need):
                if right - left < len_best:
                    best = s[left:right+1]
                    len_best = right-left
                left += 1
                if s[left-1] in window:
                    window[s[left-1]] -= 1
                    if window[s[left-1]] == need[s[left-1]] -1:
                        formed -= 1
                        break
                
                
        
        return best
                
        