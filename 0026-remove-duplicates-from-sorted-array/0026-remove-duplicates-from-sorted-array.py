class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        seen = {}
        count = 0
        for element in nums:
            if element in seen:
                continue
            else:
                seen[element] = element
                count += 1

        nums[:count] = list(seen.values())
        return count

        