class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        subset_sum, reminder = divmod(sum(nums), k)
        if reminder: return False

        # optional pre-pruning
        for num in nums:
            if num > subset_sum: return False
            if num == subset_sum: k -= 1
            if k == 0 or k == 1: return True
        
        nums = sorted([num for num in nums if num < subset_sum], reverse=True)

        used = [0] * len(nums)

        def backtrack(i, group, accum):
            if group == k: return True
            if accum > subset_sum: return False
            if accum == subset_sum: return backtrack(0, group + 1, 0)
            last_used = None
            for j, num in enumerate(nums[i:], i):
                if used[j]: continue
                if num == last_used: continue
                last_used = num
                used[j] = 1
                if backtrack(j, group, accum + nums[j]): return True
                used[j] = 0
            return False
        return backtrack(0, 0, 0)
