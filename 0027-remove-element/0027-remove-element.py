class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        dummy = []
        k = 0
        for element in nums:
            if element != val:
                dummy.append(element)
                k+= 1
        
        nums[:] = dummy
        return k