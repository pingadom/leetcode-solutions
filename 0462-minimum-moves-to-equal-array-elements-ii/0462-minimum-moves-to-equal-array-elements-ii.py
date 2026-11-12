class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums = sorted(nums)
        mid = nums[len(nums)//2]
        return sum(list(map(lambda x : abs(mid - x),nums)))