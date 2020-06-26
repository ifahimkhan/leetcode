class Maxpq:
    def __init__(self):
        self.container = []
        
    def front(self):
        # when there is no active building the skyline is ground. 
        return 0 if not self.container else -self.container[0]
    
    def push(self, h):
        heapq.heappush(self.container, -h)
    
    def remove(self, h): 
        self.container.remove(-h)
        heapq.heapify(self.container)


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = [] # x location, height, event type(-1 is start, 1 is end)
        for l, r, h in buildings:
            events.append((l, h, -1))
            events.append((r, h, 1))
        # sort by 
        # 1. x - we sweep line from left to right
        # 2. event type - we add building before remove
        # 3. height - for start event we do tallest to shortest, for end event we do the opposite
        events.sort(key=lambda x: [x[0], x[2], x[2] * x[1]])
        
        skyline, pq = [], Maxpq()
        for x, h, t in events:
            if t == -1: 
                if h > pq.front(): skyline.append([x, h])
                pq.push(h)
            else:
                pq.remove(h)
                if h > pq.front(): skyline.append([x, pq.front()])
        return skyline