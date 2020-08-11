class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        accum = [nums[0]]
        # for num in nums[1:]: # slice creates a copy of references?
        #     accum.append(accum[-1] + num)
        for i in range(1, len(nums)):
            accum.append(accum[-1] + nums[i])
        return accum
