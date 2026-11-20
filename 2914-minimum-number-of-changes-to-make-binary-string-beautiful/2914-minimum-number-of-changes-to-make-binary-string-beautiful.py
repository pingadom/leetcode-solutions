class Solution:
    def minChanges(self, s: str) -> int:
        subs = []
        moves = 0

        if len(set(s)) == 1:
            return 0

        curr = s[0]
        last = 0
        for n in range(1,len(s)):
            print(s[n])
            if s[n] != curr:
                subs.append(n-last)
                curr = s[n]
                last = n
        subs.append(n+1-last)

        
        temp = subs[0]
        odd = (temp % 2)
        for i in range(1,len(subs)):
            odd_c = subs[i] % 2
            if odd_c == 0 and odd == 0:
                continue
            elif odd and not odd_c:
                subs[i-1] += 1
                subs[i] -= 1
                moves += 1
            elif odd and odd_c:
                subs[i-1] += 1
                subs[i] -= 1
                moves += 1
            odd = subs[i] % 2

        
        return moves

            
