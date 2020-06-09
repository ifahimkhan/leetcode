class HeapQueue(object):
    from operator import lt, gt
    comparators = {'min': lt, 'max': gt}

    def __init__(self, data=None, comparator='min'):
        self._heapq = [None] + list(data) if data else [None]
        self._comparator = self.comparators.get(comparator, comparator)
        self._n = len(self._heapq) - 1
        if data: self.heapify()

    def _compare(self, i, j):
        return self._comparator(self._heapq[i], self._heapq[j])

    def __len__(self):
        return self._n

    def is_empty(self):
        return self._n == 0

    def _swap(self, i, j):
        self._heapq[i], self._heapq[j] = self._heapq[j], self._heapq[i]

    def front(self):
        assert not self.is_empty(), 'heapq is empty'
        return self._heapq[1]

    def enqueue(self, x):
        self._heapq.append(x)
        self._n += 1
        self.swim(self._n)

    def dequeue(self):
        assert not self.is_empty(), 'heapq is empty'
        self._swap(1, self._n)
        self._n -= 1
        self.sink(1)
        return self._heapq.pop()

    def swim(self, k):
        while k > 1 and self._compare(k, k >> 1):
            self._swap(k, k >> 1); k >>= 1

    def sink(self, k):
        n = self._n
        while k * 2 <= n:
            j = k * 2
            if j < n and self._compare(j + 1, j): j += 1
            if self._compare(k, j): break
            self._swap(k, j); k = j

    def heapify(self):
        for k in range(self._n >> 1, 0, -1):
            self.sink(k)

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = HeapQueue()
        for num in nums: self.add(num)

    def add(self, val: int) -> int:
        pq, k = self.pq, self.k
        if len(pq) < k or val > pq.front(): pq.enqueue(val)
        if len(pq) > k: pq.dequeue()
        return pq.front()
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)