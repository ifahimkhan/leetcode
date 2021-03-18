class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        
        def get_sign(n1, n2):
            if n2 > n1: return 1
            if n2 == n1: return 0
            if n2 < n1: return -1
                
        strike = 1
        sign = None
        for i in range(n-1):
            new_sign = get_sign(nums[i], nums[i + 1])
            if (sign is None and new_sign != 0) or\
               (sign and new_sign * sign == -1):
                strike += 1
                sign = new_sign
        return strike
