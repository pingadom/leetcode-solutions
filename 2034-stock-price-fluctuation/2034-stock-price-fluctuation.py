import heapq

class StockPrice:

    def __init__(self):
        self.latest = 0
        self.seen = {}
        self.maxi_p = []
        self.mini_p = []

    def update(self, timestamp: int, price: int) -> None:
        self.latest = max(self.latest, timestamp)
        self.seen[timestamp] = price

        heapq.heappush(self.maxi_p, (-price, timestamp))
        heapq.heappush(self.mini_p, (price, timestamp))

    def current(self) -> int:
        return self.seen[self.latest]

    def maximum(self) -> int:
        while True:
            price, timestamp = self.maxi_p[0]

            if -price == self.seen[timestamp]:
                return -price

            heapq.heappop(self.maxi_p)

    def minimum(self) -> int:
        while True:
            price, timestamp = self.mini_p[0]

            if price == self.seen[timestamp]:
                return price

            heapq.heappop(self.mini_p)