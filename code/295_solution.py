class MedianFinder:    
    def __init__(self):
        """ initialize your data structure here. """
        self.max_heap = []   
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if not self.max_heap or -1 * self.max_heap[0] >= num:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        #balancing max and min heap
        if len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        elif len(self.max_heap) - len(self.min_heap) == 2:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))


    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
