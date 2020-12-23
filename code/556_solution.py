class Solution:
    def nextGreaterElement(self, n: int) -> int:
        def swap(a, i, j):
            a[i], a[j] = a[j], a[i]        
            
        def reverse(a, f=None, t=None):
            l = f if f else 0
            r = t if t else len(a) - 1
            while l < r:
                swap(a, l, r)
                l += 1
                r -= 1
                
        nums = list(str(n))
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]: i -= 1
        
        # find the rightmost upward step
        for l in range(len(nums) - 2, -1, -1):
            if nums[l] < nums[l + 1]: break
        else:
            # must be decreasing all the way from left to right
            return -1 
        
        # find the smallest number from right that is larger than the number find above
        for r in range(len(nums) - 1, l, -1):
            if nums[r] > nums[l]: break
        
        swap(nums, l, r)
        reverse(nums, l + 1)
        m = int(''.join(nums))
        return m if m < 2 ** 31 - 1 else -1        
