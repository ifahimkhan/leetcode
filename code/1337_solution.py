class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:       
        powers = defaultdict(list)
        for i, row in enumerate(mat): powers[sum(row)].append(i)
        order = sum([powers[i] for i in range(len(mat[0]) + 1)], [])
        return order[:k]
    
        # return sorted(range(len(mat)), key=lambda x: sum(mat[x]))[:k]
