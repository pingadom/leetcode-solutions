
from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dq = deque()
        cost = 0
        ans = 0
        right = n - 1

        for left in range(n - 1, -1, -1):

            # Add nums[left] to the window
            while dq and nums[dq[0]] <= nums[left]:
                p = dq.popleft()
                end = dq[0] if dq else right + 1

                cost += (nums[left] - nums[p]) * (end - p)

            dq.appendleft(left)

            # Shrink window until cost <= k
            while cost > k:
                cost -= nums[dq[-1]] - nums[right]

                if dq[-1] == right:
                    dq.pop()

                right -= 1

            # Count valid subarrays starting at left
            ans += right - left + 1

        return ans
