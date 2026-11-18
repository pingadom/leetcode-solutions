import heapq

class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        min_q = []
        max_q = []
        best = 0
        l = 0

        for r, v in enumerate(nums):
            heapq.heappush(min_q, (v, r))
            heapq.heappush(max_q, (-v, r))

            while -max_q[0][0] - min_q[0][0] > limit:
                l += 1

                while max_q and max_q[0][1] < l:
                    heapq.heappop(max_q)

                while min_q and min_q[0][1] < l:
                    heapq.heappop(min_q)

            best = max(best, r - l + 1)

        return best