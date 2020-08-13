class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.k = combinationLength
        self.n= len(characters)
        self.chars = list(characters)
        self.__iter__()
    
    def __next__(self):
        combo = ''.join(map(self.chars.__getitem__, self.p))
        p, n, k = self.p, self.n, self.k
        j = k - 1
        while j >= 0 and p[j] == n - k + j: j -= 1
        p[j] += 1
        
        if j >= 0: 
            for i in range(j + 1, k): p[i] = p[j] + i - j
        else:
            self._has_next = False
        return combo
    
    def __iter__(self): 
        self.p = list(range(self.k))
        self._has_next = True
        
    next = __next__

    def hasNext(self): return self._has_next


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()