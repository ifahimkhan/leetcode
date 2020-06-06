# 0. Ignore the initially infected nodes, and find all CCs in the reminder
# 1. Find the initial infected nodes each CC are connected to.
# 2a. Filter the CCs to keep only the CCs that has one adjacency initial infected node.
    # note remove that adjacency node, the whole CC will be safe
# 2b. From above, get initial infected node -> list of size of filtered CCs.
# 4. Find the node with the max sum from list of sizes, choose smaller index when tire. 


class UnionFind(object):
    def __init__(self, n):
        self.parents = list(range(n))
        self.sizes = [1] * n

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
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        uf = UnionFind(n)
        initial = set(initial)
        # find all CCs ignore the initial infected nodes O(N^2)
        for i in range(n):
            if i in initial: continue
            for j in range(n):
                if j in initial: continue
                if graph[i][j]: uf.union(i, j)
        
        # annotate initial infected nodes to CCs O(initial * N)
        adj_infected = collections.defaultdict(list)
        for i in initial:
            for j in range(n):
                if i == j: continue
                if j in initial: continue
                if graph[i][j] == 1: adj_infected[uf.find(j)].append(i)
                    
        # filter the CCs, and create node to potential saves mapping
        node_potentials = collections.defaultdict(list)
        for cc, nodes in adj_infected.items():
            if len(nodes) != 1: continue
            node_potentials[nodes[0]].append(uf.sizes[cc])
        
        # find the optimal removal node
        max_size, candidate = 0, min(initial)
        for i, potentials in node_potentials.items():
            size = sum(potentials)
            if size > max_size:
                max_size, candidate = size, i
            elif size == max_size and i < candidate:
                candidate = i
        return candidate
