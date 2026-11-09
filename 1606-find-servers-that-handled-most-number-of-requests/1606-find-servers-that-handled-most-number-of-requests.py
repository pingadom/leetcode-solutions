import heapq

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        arrival_count = {}
        for p in range(k):
            arrival_count[p] = 0
        t = 0
        heap_available = list(range(k))
        heapq.heapify(heap_available)
        heap_busy = []

        for i in range(len(arrival)):
            t = arrival[i]

            while len(heap_busy) > 0 and heap_busy[0][0] <= t:
                finish, server = heapq.heappop(heap_busy)
                heapq.heappush(heap_available, i + (server - i) % k)

            if not heap_available:
                continue

            server = heapq.heappop(heap_available) % k

            heapq.heappush(heap_busy, (arrival[i] + load[i], server))
            arrival_count[server] += 1
        
        maximum = max(arrival_count.values())
        indices = [i for i, x in arrival_count.items() if x == maximum]
        return indices
        
        