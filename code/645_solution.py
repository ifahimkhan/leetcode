# if allow modify array, use sign trick to find duplicate
# otherwise use a set to find duplicate with additional O(n) space. 


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        delta = sum(range(1, n + 1)) - sum(nums)
        
        for i in range(n):
            if nums[abs(nums[i]) - 1] < 0: break
            nums[abs(nums[i])-1] *= -1
        
        duplicated = abs(nums[i])
        
        return (duplicated, duplicated + delta)
