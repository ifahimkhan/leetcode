class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        result = nums[0] + nums[1] + nums[-1]
        
        for i in range(n - 2):
            j, k = i + 1, n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                
                if total == target: return total
                if abs(total - target) < abs(result - target): result = total
                    
                if total < target: j += 1
                else: k -= 1
                    
        return result
