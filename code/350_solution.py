class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2 = sorted([nums1, nums2], key=len)
        freq = collections.Counter(nums1)
        
        result = []
        for num in filter(lambda x: x in freq, nums2):
            freq[num] -= 1
            if freq[num] >= 0: result.append(num)
                
        return result