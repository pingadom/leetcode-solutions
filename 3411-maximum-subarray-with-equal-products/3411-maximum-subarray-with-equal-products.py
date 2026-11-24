class Solution:
    def maxLength(self, nums: List[int]) -> int:
        for n in range(len(nums)-1,0,-1):
            p1,p2 = 0,n
            while p2 < len(nums):
                t = nums[p1:p2+1]
                if prod(t) == gcd(*t)*lcm(*t):
                    return p2-p1 + 1
                p1 += 1
                p2 += 1
