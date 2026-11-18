from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1

        count,total = 0,0
        i = 0

        while i < len(nums):
            total += nums[i]
            count += seen[total-k]
            seen[total] += 1
            i += 1
        
        return count
        