class MyCircularQueue:
    def __init__(self, k: int):
        self.capacity = k
        self.queue = [0] * k
        self.first = 0
        self.n = 0

    def enQueue(self, value: int) -> bool:
        if self.n == self.capacity: return False
        self.queue[(self.first + self.n) % self.capacity] = value
        self.n += 1
        return True

    def deQueue(self) -> bool:
        if self.n == 0: return False
        self.first = (self.first + 1) % self.capacity
        self.n -= 1
        return True

    def Front(self) -> int:
        if self.n == 0: return -1
        return self.queue[self.first]

    def Rear(self) -> int:
        if self.n == 0: return -1
        return self.queue[(self.first + self.n - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.n == 0

    def isFull(self) -> bool:
        return self.n == self.capacity
