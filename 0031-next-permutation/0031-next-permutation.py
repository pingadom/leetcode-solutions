class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        length = len(nums)

        for n in range(length - 1, 0, -1):
            if nums[n] > nums[n-1]:
                pivot = n - 1

                # Find smallest element larger than pivot
                for j in range(length - 1, pivot, -1):
                    if nums[j] > nums[pivot]:
                        nums[pivot], nums[j] = nums[j], nums[pivot]
                        break

                # Reverse everything after pivot
                nums[pivot+1:] = nums[pivot+1:][::-1]
                return

        # Entire array is descending
        nums[:] = nums[::-1]