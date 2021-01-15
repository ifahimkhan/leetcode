class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0] * (n+2)
        nums[1] = 1
        for i in range(2, n+1):
            if i % 2:
                nums[i] = nums[i>>1] + nums[(i>>1)+1]
            else:
                nums[i] = nums[i>>1]
        return max(nums[:n+1])
