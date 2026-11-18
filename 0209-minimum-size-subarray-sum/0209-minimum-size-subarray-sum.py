class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = total = 0
        best = float('inf') 

        for right,num in enumerate(nums):
            total += num

            while total >= target:

                if right-left < best:
                    best = right - left + 1
                total -= nums[left]

                left += 1
        
        if best == float('inf'):
            return 0
        else:
            return best

        