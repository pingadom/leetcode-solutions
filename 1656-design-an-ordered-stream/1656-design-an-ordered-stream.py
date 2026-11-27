class OrderedStream:

    def __init__(self, n: int):
        self.keys = [""]*(n+1)
        self.count = 1

    def insert(self, idKey: int, value: str) -> list[str]:
        ret = []
        self.keys[idKey] = value
        if idKey == self.count:
            for n in range(idKey,len(self.keys)):
                if self.keys[n] == "":
                    break
                ret.append(self.keys[n])
            self.count = n
        return ret
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)