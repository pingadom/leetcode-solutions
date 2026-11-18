class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        left,right = 0,k-1
        s = sum(nums[left:right+1])
        best = s/k

        while right < len(nums)-1:
            s += nums[right+1] - nums[left]
            left += 1
            right += 1

            best = max(best,s/k)
        
        return best
            
        