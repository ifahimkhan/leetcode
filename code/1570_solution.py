# hash map: index to value
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
        
# list of indices and list of values. Or can be list of (idx, value) pair. 
class SparseVector:
    def __init__(self, nums: List[int]):
        self.indices = []
        self.values = []
        for idx, num in enumerate(nums):
            if num == 0: continue
            self.indices.append(idx)
            self.values.append(num)

    def __len__(self): return len(self.indices)

    def dotProduct(self, vec: 'SparseVector') -> int:
        product = 0
        l1, l2 = 0, 0
        while l1 < len(self) and l2 < len(vec):
            if self.indices[l1] == vec.indices[l2]:
                product += self.values[l1] * vec.values[l2]
                l1 += 1
                l2 += 1
            elif self.indices[l1] < vec.indices[l2]:
                l1 += 1
            elif self.indices[l1] > vec.indices[l2]:
                l2 += 1
        return product        
        
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
