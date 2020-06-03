class UnionFind(object):
    def __init__(self, nums=None):
        self.parents = dict()
        self.sizes = dict()
        if nums: list(map(self.insert, nums))
        
    def insert(self, i):
        self.parents[i], self.sizes[i] = i, 1

    def find(self, i):
        if i not in self.parents: self.insert(i)
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

        
# The offline union find solution
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         uf = UnionFind(nums)  # O(N)
#         for num in nums: # O(N)
#             # if num + 1 in uf.parents:
#             #     uf.union(num, num + 1)
#             if num - 1 in uf.parents: continue
#             while num + 1 in uf.parents:
#                 uf.union(num, num + 1)
#                 num += 1
#         return max(uf.sizes.values()) if uf.sizes else 0

# # The union find solution leads to this hash set solution natually.    
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         nums = set(nums)
#         max_len = 0
#         for num in nums:
#             if num - 1 in nums: continue
#             l = 1
#             while num + 1 in nums:
#                 l += 1
#                 num += 1
#             max_len = max(max_len, l)
#         return max_len

# The online solution using union find
# can be further analyzed and optimized to a hash table only solution.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UnionFind()  
        for num in nums: # O(N)
            if num not in uf.parents: uf.insert(num)
            if num + 1 in uf.parents: uf.union(num, num + 1)
            if num - 1 in uf.parents: uf.union(num, num - 1)
        return max(uf.sizes.values()) if uf.sizes else 0
