class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        results = []
        i = 1
        while k > 1:
            results.extend([i, i + k])
            i += 1
            k -= 2
        results.extend(range(i, n+1))
        return results
                
