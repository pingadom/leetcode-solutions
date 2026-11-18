from collections import Counter

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        seen2 = {}
        stack = []
        answer = [-1] * len(nums2)
        for i,v in enumerate(nums2):
            seen2[v] = i
            while stack and stack[-1][0] < v:
                _,p = stack.pop()
                answer[p] = v
            stack.append((v,i))
        
        final = []
        for e in nums1:
            final.append(answer[seen2[e]])
        
        return final
        
        


            
        