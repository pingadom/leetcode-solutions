from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1,l2 = len(s1),len(s2)
        left,right = 0,len(s1)-1
        check = Counter(s1)
        print(check, Counter(s2[left:right]))

        while right < len(s2):
            print(left,right)
            if Counter(s2[left:right+1]) <= check:
                return True
            right += 1
            left +=1
        
        return False
        
        