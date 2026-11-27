import heapq
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        small = []  # max heap
        large = []  # min heap
        delayed = defaultdict(int)

        small_size = 0
        large_size = 0
        res = []

        def prune(heap, sign):
            while heap:
                val = heap[0] * sign

                if delayed[val] == 0:
                    break

                heapq.heappop(heap)
                delayed[val] -= 1

        def balance():
            nonlocal small_size, large_size

            if small_size > large_size + 1:
                heapq.heappush(large, -heapq.heappop(small))
                small_size -= 1
                large_size += 1
                prune(small, -1)

            elif small_size < large_size:
                heapq.heappush(small, -heapq.heappop(large))
                large_size -= 1
                small_size += 1
                prune(large, 1)

        def add(num):
            nonlocal small_size, large_size

            if not small or num <= -small[0]:
                heapq.heappush(small, -num)
                small_size += 1
            else:
                heapq.heappush(large, num)
                large_size += 1

            balance()

        def remove(num):
            nonlocal small_size, large_size

            delayed[num] += 1

            if num <= -small[0]:
                small_size -= 1

                if num == -small[0]:
                    prune(small, -1)
            else:
                large_size -= 1

                if num == large[0]:
                    prune(large, 1)

            balance()

        for i in range(k):
            add(nums[i])

        for i in range(k, len(nums) + 1):

            if k % 2:
                res.append(-small[0])
            else:
                res.append((-small[0] + large[0]) / 2)

            if i < len(nums):
                add(nums[i])
                remove(nums[i - k])

        return res