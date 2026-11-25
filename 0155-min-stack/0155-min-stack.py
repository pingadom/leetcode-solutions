class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = [float("inf")]
        

    def push(self, value: int) -> None:
        if value <= self.minstack[-1]:
            self.minstack.append(value)
        self.stack.append(value)
        #print(self.stack,self.minstack)
        
    def pop(self) -> None:
        #print('pop',self.stack[-1])
        if self.stack:
            temp = self.stack.pop()
        if temp == self.minstack[-1]:
            self.minstack.pop()
        #print(self.stack,self.minstack)
        

    def top(self) -> int:
        #print('check top',self.stack[-1])
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        #print('check min',self.minstack[-1])
        if self.minstack:
            return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()