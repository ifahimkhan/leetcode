class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.ranges = [0]
        
        prefix_sum = 0
        for x1, y1, x2, y2 in rects:
            prefix_sum += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.ranges.append(prefix_sum)

    def pick(self) -> List[int]:
        n = random.randint(1, self.ranges[-1])
        i = bisect.bisect_left(self.ranges, n)
        x1, y1, x2, y2 = self.rects[i - 1]
        return [random.randint(x1, x2), random.randint(y1, y2)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()