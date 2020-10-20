class Solution:
    def solution_constant_space(self, nums):
        # O(N^2) Time O(1) Space
        return sum(nums[i] == nums[j] for i in range(len(nums)) for j in range(i+1, len(nums)))
    
    def solution_map(self, nums):
        # O(N) Time O(N) Space
        return sum(v * (v - 1) // 2 for v in Counter(nums).values())
    
    
    
    numIdenticalPairs = solution_constant_space # solution_map
