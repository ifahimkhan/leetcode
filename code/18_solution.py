class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:   
        def two_sum(nums, target):
            n = len(nums)
            l, r = 0, n - 1
            pairs = []
            while l < r:
                s = nums[l] + nums[r]
                if s > target or (r < n - 1 and nums[r] == nums[r + 1]):
                    r -= 1
                elif s < target or (l > 0 and nums[l] == nums[l - 1]):
                    l += 1
                else:
                    pairs.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
            return pairs
        
        def k_sum(nums, target, k):
            if len(nums) == 0: return []
            if nums[0] > target / k or nums[~0] < target / k: return []           
            result = []
            if k == 2: return two_sum(nums, target)
            for i, num in enumerate(nums):
                if i == 0 or nums[i - 1] != num:
                    for pair in k_sum(nums[i + 1:], target - num, k - 1):
                        result.append([num] + pair)
            return result
        
        nums.sort()
        return k_sum(nums, target, 4)
