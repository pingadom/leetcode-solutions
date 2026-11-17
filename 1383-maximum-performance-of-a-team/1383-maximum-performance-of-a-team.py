from heapq import heappop, heappush, heapify

class Solution:
    def maxPerformance(self, n: int, speed: list[int], efficiency: list[int], k: int) -> int:
        modulo = 10**9 + 7
        maxheap = []
        speed_sum = 0
        res = 0

        zipped = zip(efficiency,speed)
        for e,s in zipped:
            heappush(maxheap,(-e,s))

        minheap = []
        speed_sum = 0

        while maxheap:
            e,s = heappop(maxheap)
            e = -e
            
            heappush(minheap,s)
            speed_sum += s

            if len(minheap) > k:
                speed_sum -= heappop(minheap)
            
            res = max(res, speed_sum * e)
        
        return res % modulo
                
        


        