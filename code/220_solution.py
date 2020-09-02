class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        def get_id(x, w):
            return (x + 1) // w - 1 if x < 0 else x // w
    
        if t < 0: return False
        d = dict()
        w = t + 1
        for i in range(len(nums)):
            m = get_id(nums[i], w)
            if m in d: return True
            if (m - 1) in d and abs(nums[i] - d[m - 1]) < w: return True
            if (m + 1) in d and abs(nums[i] - d[m + 1]) < w: return True
            d[m] = nums[i]
            if i >= k: d.pop(get_id(nums[i - k], w))
        return False
    
