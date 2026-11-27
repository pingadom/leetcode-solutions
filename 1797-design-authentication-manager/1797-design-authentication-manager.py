class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.token_time = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.token_time[tokenId] = currentTime+self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.token_time:
            et = self.token_time[tokenId]
            if currentTime >= et:
                return
            else:
                self.token_time[tokenId] = currentTime + self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        #print(self.token_time)
        #print([x for _,x in self.token_time.values() if x >= currentTime])
        return len([x for x in self.token_time.values() if x > currentTime])


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)