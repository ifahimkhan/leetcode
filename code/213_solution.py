class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) <= 3: return max(nums)

        def dp(start, finish):
            do, rest = 0, 0
            for i in range(start, finish):
                do, rest = rest + nums[i], max(rest, do)
            return max(rest, do)
        
        return max(dp(0, len(nums)-1), dp(1, len(nums)))
