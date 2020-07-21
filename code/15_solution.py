class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3: return []
        n = len(nums)    
        nums.sort() # O(NlogN)
        triplets = []
        
        def find_two_sum(j, k, target):
            while j < k:
                b, c = nums[j], nums[k]
                if b + c > target:
                    while j < k and nums[k] == c: k -= 1
                elif b + c < target:
                    while j < k and nums[j] == b: j += 1
                else:
                    triplets.append([-target, b, c])
                    while j < k and nums[k] == c: k -= 1
                    while j < k and nums[j] == b: j += 1

        i = 0
        while i < n - 2 and nums[i] <= 0:
            a, target = nums[i], -nums[i] 
            find_two_sum(i+1, n-1, target)
            while i < n - 2 and nums[i] == a: i += 1
        
        return triplets