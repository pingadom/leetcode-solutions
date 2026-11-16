class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left, right = 0, len(nums) - 1
        first = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

            if nums[mid] == target:
                first = mid

        left, right = 0, len(nums) - 1
        last = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

            if nums[mid] == target:
                last = mid

        return [first, last]