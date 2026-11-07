
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # No triplet can sum to zero
            if nums[i] > 0:
                break

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append(
                        [nums[i], nums[left], nums[right]]
                    )

                    left += 1
                    right -= 1

                    # Skip duplicate second numbers
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate third numbers
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result
