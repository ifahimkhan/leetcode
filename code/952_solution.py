class UnionFind(object):
    def __init__(self, n):
        self.parents = list(range(n+1))
        self.sizes = [1] * (n + 1)

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
    def largestComponentSize(self, A: List[int]) -> int:
        uf = UnionFind(max(A))
        
        for num in A:
            for factor in range(2, int(num ** .5) + 1):
                if num % factor == 0:
                    uf.union(num, factor)
                    uf.union(num, num // factor)
        
        group_count = dict()
        for num in A:
            root = uf.find(num)
            group_count[root] = group_count.get(root, 0) + 1
        return max(group_count.values())
