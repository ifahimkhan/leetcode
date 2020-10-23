class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3: return False
        
        curr_min = nums[0]
        prefix_min = []
        for num in nums: 
            curr_min = min(curr_min, num)
            prefix_min.append(curr_min)
        
        k = n
        for j in range(n - 1, -1, -1):
            if nums[j] <= prefix_min[j]: continue
            while k < n and nums[k] <= prefix_min[j]: k += 1
            if k < n and nums[k] < nums[j]: return True
            k -= 1
            nums[k] = nums[j]
        return False
