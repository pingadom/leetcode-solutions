class Solution:
    def findMin(self, nums: list[int]) -> int:
        left,right = 0,len(nums)-1
        mid = (left+right)//2
        prev = -1

        while prev != mid:
            if nums[right] < nums[mid]:
                left = mid
            elif nums[left] > nums[mid]:
                right = mid
            prev = mid
            mid = (left+right)//2
        return min(nums[left],nums[right],nums[mid])
        