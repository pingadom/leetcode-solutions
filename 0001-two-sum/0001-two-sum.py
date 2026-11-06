class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(0,len(nums)):
            if (target - nums[i]) in seen:
                return[i,seen[target - nums[i]]]
            seen[nums[i]]=i