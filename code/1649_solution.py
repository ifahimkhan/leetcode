class BinaryIndexedTree(object):
    def __init__(self, m):
        self.m = m
        self.bit = [0] * (m + 1)
    
    def update(self, i):
        while i <= self.m:
            self.bit[i] += 1
            i += i & - i
            
    def get(self, i):
        total = 0
        while i > 0:
            total += self.bit[i]
            i -= i & -i
        return total

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        tree = BinaryIndexedTree(max(instructions))
        
        cost = 0
        for i, num in enumerate(instructions):
            cost += min(tree.get(num - 1), i - tree.get(num))
            tree.update(num)
        return cost % (10**9 + 7)
