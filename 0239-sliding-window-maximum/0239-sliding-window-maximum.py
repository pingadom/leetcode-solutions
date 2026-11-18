from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq, out = deque(), []          # indices, values decreasing front to back
        for i, x in enumerate(nums):
            while dq and nums[dq[-1]] <= x:
                dq.pop()                  # smaller values can never be a maximum again
            dq.append(i)
            if dq[0] <= i - k:
                dq.popleft()              # the front has left the window
            if i >= k - 1:
                out.append(nums[dq[0]])
        return out
        