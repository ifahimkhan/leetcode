MOD = 10 ** 9 + 7

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        l, r = 0, n - 1
        total = 0
        while l <= r:
            while l < r and nums[l] + nums[r] > target:  
                r -= 1
            if l <= r and nums[l] + nums[r] <= target: 
                # total += 2 ** (r - l) % MOD
                total += pow(2, r - l, MOD)
            l += 1
        return total % MOD         
