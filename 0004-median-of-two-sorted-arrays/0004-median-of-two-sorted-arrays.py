
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Always binary search the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n

        mini = 0
        maxi = m

        while mini <= maxi:
            # Determine partition positions
            p1 = (mini + maxi) // 2
            p2 = (total + 1) // 2 - p1

            # Values immediately around each partition
            l1 = nums1[p1 - 1] if p1 > 0 else float("-inf")
            r1 = nums1[p1] if p1 < m else float("inf")

            l2 = nums2[p2 - 1] if p2 > 0 else float("-inf")
            r2 = nums2[p2] if p2 < n else float("inf")

            # Correct partition found
            if l1 <= r2 and l2 <= r1:
                if total % 2 == 1:
                    return float(max(l1, l2))
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2

            # Too many elements taken from nums1
            elif l1 > r2:
                maxi = p1 - 1

            # Too few elements taken from nums1
            else:
                mini = p1 + 1

        raise ValueError("Input arrays must be sorted")
