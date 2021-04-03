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
    def largestIsland(self, grid: List[List[int]]) -> int:        
        nrows, ncols = len(grid), len(grid[0])
        
        def get_neighbors(r, c):
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < nrows and 0 <= nc < ncols:
                    yield nr, nc
                    
        uf = UnionFind()
        
        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c]: 
                    uf.insert((r, c)) 
                    for nr, nc in get_neighbors(r, c):
                        if grid[nr][nc]:
                            uf.insert((nr, nc))       
                            uf.union((r,c), (nr, nc))
                        
        
        max_size = 0 if not uf.sizes else max(uf.sizes.values())
        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c]: continue
                
                neighbor_info = dict()
                for loc in get_neighbors(r, c):
                    if loc not in uf:
                        neighbor_info[loc] = 0
                    else:
                        island_id = uf.find(loc)                        
                        neighbor_info[island_id] = uf.sizes[island_id]
                max_size = max(max_size, 1 + sum(neighbor_info.values(), 0))

        return max_size
