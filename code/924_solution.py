# 0. Find all CCs  n^2 time
# 1. Find the CC with only one initial infection O(initial)
# 2a. Find the largest among above  O(num_cc)
# 2b. If there are tires, we choose smaller index 

class UnionFind(object):
    def __init__(self, n):
        self.parents = list(range(n))
        self.sizes = [1] * n

    def find(self, i):
        while i != self.parents[i]:
            # path compression, have i points to the cluster centroid
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
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        uf = UnionFind(n)
        # find all ccs O(N^2)
        for i in range(n):
            for j in range(n):
                if graph[i][j]: uf.union(i, j)
        
        # count the number of initial infected nodes each cc has
        infected = collections.defaultdict(lambda:0)
        for i in initial: infected[uf.find(i)] += 1
        
        # Find the largest among above  O(num_cc)
        # return smallest index if there are tires
        max_size, candidate = 0, min(initial)
        for i in initial:
            infection_count = infected[uf.find(i)]
            size = uf.sizes[uf.find(i)]
            if infection_count != 1: continue
            if size > max_size:
                max_size, candidate = size, i
            elif size == max_size and i < candidate:
                candidate = i
        return candidate
