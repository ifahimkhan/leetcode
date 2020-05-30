class Solution(object):
    def smallestDistancePair(self, nums, k):
        def possible(guess):
            count, l = 0, 0 
            for r, x in enumerate(nums):
                while x - nums[l] > guess: l += 1
                count += r - l
            return count >= k

        nums.sort()
        l = 0
        h = nums[-1] - nums[0]
        while l < h:
            mid = (l + h) // 2
            if possible(mid): h = mid
            else: l = mid + 1
        return l