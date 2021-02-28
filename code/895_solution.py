class FreqStack:
    def __init__(self):
        self.freq = dict()
        self.buckets = defaultdict(list)
        self.max_freq = 0

    def push(self, x):
        self.freq[x] = self.freq.get(x, 0) + 1
        self.max_freq = max(self.max_freq, self.freq[x])
        self.buckets[self.freq[x]].append(x)
        
    def pop(self):
        x = self.buckets[self.max_freq].pop()
        if len(self.buckets[self.max_freq]) == 0: 
            self.max_freq -= 1
        self.freq[x] -= 1
        return x
        

# priority queue + hash map
# class FreqStack:
#     def __init__(self):
#         self.freq = dict()
#         self.pq = []
#         self.i = 0

#     def push(self, x: int) -> None:
#         self.freq[x] = self.freq.get(x, 0) + 1
#         self.i += 1
#         heappush(self.pq, [-self.freq[x], -self.i, x])
#         # print(self.freq, self.pq)

#     def pop(self) -> int:
#         _, _, x = self.pq[0]
#         heappop(self.pq)
#         self.freq[x] -= 1
#         return x
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
