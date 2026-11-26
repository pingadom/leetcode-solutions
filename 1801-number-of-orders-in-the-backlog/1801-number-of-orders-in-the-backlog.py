import heapq

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy = []
        sell = []
        mod = 10**9 + 7

        for order in orders:
            p,v,t = order
            while v > 0:
                if t == 1:
                    if buy and -buy[0][0] >= p:
                        if v < buy[0][1]:
                            tp,tv = heapq.heappop(buy)
                            heapq.heappush(buy,(tp,tv-v))
                            break
                        else:
                            _,tv = heapq.heappop(buy)
                            v -= tv
                    else:
                        heapq.heappush(sell,(p,v))
                        break
                else:
                    if sell and sell[0][0] <= p:
                        if v < sell[0][1]:
                            tp,tv = heapq.heappop(sell)
                            heapq.heappush(sell,(tp,tv-v))
                            break
                        else:
                            _,tv = heapq.heappop(sell)
                            v -= tv
                    else:
                        heapq.heappush(buy,(-p,v))
                        break

        return (sum(x[1] for x in buy) +
        sum(x[1] for x in sell)) % (10**9 + 7)
                
        