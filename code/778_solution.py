class UnionFind(object):
    def __init__(self):
        self.parents = dict()
        self.sizes = dict()
        
    def __contains__(self, i):
        return i in self.parents
    
    def insert(self, i):
        if self.__contains__(i): return
        self.parents[i] = i
        self.sizes[i] = 1
        
    def find(self, i):
        while i != self.parents[i]:
            self.parents[i] = self.find(self.parents[i])  
            i = self.parents[i]
        return i

    def union(self, p, q):
        root_p, root_q = map(self.find, (p, q))
        if root_p == root_q: return
        small, big = sorted([root_p, root_q], key=lambda x: self.sizes[x])
        self.parents[small] = big
        self.sizes[big] += self.sizes[small]    

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        t_to_loc = {grid[r][c]: (r,c) for r in range(n) for c in range(n)}
        uf = UnionFind()
        for t in range(n**2):
            r, c = t_to_loc[t]
            uf.insert((r,c))
            for rr, cc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                if (rr, cc) not in uf: continue
                uf.union((r,c), (rr,cc))
            if (0,0) in uf and (n-1,n-1) in uf and uf.find((0,0)) == uf.find((n-1,n-1)):
                return t
