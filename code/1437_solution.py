class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last = None
        for i, num in enumerate(nums):
            if num != 1: continue
            if last is not None and last + k >= i: return False
            last = i
        return True
