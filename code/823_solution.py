MOD = 10 ** 9 + 7


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        num_trees = dict()
        for num in sorted(arr):   
            num_new_trees = 1  # as leaf
            
            for left in num_trees:
                if num % left: continue 
                right = num // left
                if right not in num_trees: continue 
                num_new_trees += num_trees[left] * num_trees[right]
                
            num_trees[num] = num_new_trees
            
        return sum(num_trees.values()) % MOD
