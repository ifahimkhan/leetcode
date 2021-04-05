class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values = []

    def push(self, x: int) -> None:
        prev_max = x if not self.values else self.values[~0][1]
        self.values.append((x, max(x, prev_max)))

    def pop(self) -> int:
        return self.values.pop()[0]
        
    def top(self) -> int:
        return self.values[~0][0]

    def peekMax(self) -> int:
        return self.values[~0][1]

    def popMax(self) -> int:
        temp = deque()
        target = self.peekMax()
        while self.top() != target: temp.appendleft(self.pop())
        self.pop()
        for x in temp: self.push(x)
        return target
        
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
