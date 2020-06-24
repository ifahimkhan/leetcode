# 1 2 3 4 5
#     ^
#     root
    
# for root in range(1, 6):    
#     left = numTrees(2)
#     right = numTrees(2)
#     total += left * right

# 1 2 3 4 5
# ^
# root    

# base case
# numTrees[0] = 1    
# numTrees[1] = 1    
# --------------------------

# numTrees[n] = sum(help(root, n) for root in range(1, n+1))
# help(root, n) = numTrees[root-1] * numTrees[n-root]

# numTrees[n] = sum(numTrees[root-1] * numTrees[n-root] for root in range(1, n+1))
# numTrees[0] = 1    
# numTrees[1] = 1    

class Solution:
    # @functools.lru_cache(None)
    # def numTrees(self, n: int) -> int:
    #     if n <= 1: return 1
    #     num = 0
    #     for i in range(1, n+1):
    #         left, right = i - 1, n - i
    #         num += self.numTrees(left) * self.numTrees(right)
    #     return num
    
    def numTrees(self, n: int) -> int:
        num_trees = [0] * (n + 1)
        num_trees[0] = num_trees[1] = 1
        for i in range(2, n + 1):
            for left in range(i):
                right = i - left - 1
                num_trees[i] += num_trees[left] * num_trees[right]
        return num_trees[n]