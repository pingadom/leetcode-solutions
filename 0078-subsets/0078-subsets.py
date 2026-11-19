class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        out = []
        
        while nums:
            t = nums.pop()
            out.append([t])
            for n in range(0,len(out)-1):
                out.append(out[n] + [t])
        out.append([])
        return out