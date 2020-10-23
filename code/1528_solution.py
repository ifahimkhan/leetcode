class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [''] * len(indices)
        for i in indices:
            res[indices[i]] = s[i]
        return ''.join(res)        
