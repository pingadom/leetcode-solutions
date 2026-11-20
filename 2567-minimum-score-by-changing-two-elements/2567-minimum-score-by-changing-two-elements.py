class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) > 4:
            return min(abs(nums[-1]-nums[2]),abs(nums[-2]-nums[1]),abs(nums[-3]-nums[0]))
        else:
            return abs(nums[-1]-nums[2])
        