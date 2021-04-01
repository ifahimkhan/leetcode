class SparseVector:
    def __init__(self, nums: List[int]):
        self.idx_to_value = {i: num for i, num in enumerate(nums) if num}
        self.length = len(nums)
        
    def __getitem__(self, i): return self.idx_to_value.get(i, 0)
    
    @property
    def indices(self): return self.idx_to_value.keys()

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        assert self.length == vec.length, 'vectors have different size.'
        indices = set(self.indices).intersection(vec.indices)
        return sum([self[i] * vec[i] for i in indices])
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
