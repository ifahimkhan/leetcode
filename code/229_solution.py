class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums: return []
        
        c1, c2, e1, e2 = 0, 0, None, None
        for num in nums:
            c1 += 1 if num == e1 else 0
            c2 += 1 if num == e2 else 0
            if num != e1 and num != e2:
                if not c1: c1, e1 = 1, num
                elif not c2: c2, e2 = 1, num
                else: c1, c2 = c1 - 1, c2 - 1
        
        thresh = len(nums) // 3
        results = set(e for e in [e1, e2] if nums.count(e) > thresh)
        return results
