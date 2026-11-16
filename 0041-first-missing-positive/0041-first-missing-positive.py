class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        c = {value: None for value in nums}
        m = max(max(nums),0)
        for n in range(1,m):
            if n not in c:
                return n
        return m + 1
        