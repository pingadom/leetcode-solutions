class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s,big = set(nums), 0

        for x in s:
            if x-1 not in s:
                y = x + 1
                while y in s:
                    y+= 1
                big = max(big, y-x)
    
        return big