class Solution:
    def minMoves(self, nums: list[int]) -> int:

        min_num = min(nums)
        return sum(list(map(lambda x : x-min_num,nums)))
