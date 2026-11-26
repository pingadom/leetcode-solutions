from bisect import bisect_left,bisect_right

class TimeMap:

    def __init__(self):
        self.seen = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.seen:
            self.seen[key] = {}
        self.seen[key][timestamp] = value
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.seen:
            return ""
        times = list(self.seen[key].keys())
        i = bisect_right(times,timestamp)-1
        closest = times[i]
        return self.seen[key][closest] if i > -1 else ""
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)