class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        nrow, ncol = len(mat), len(mat[0])
        def sort_diagonal(r, c):
            numbers = sorted([mat[rr][cc] for rr, cc in zip(range(r, nrow), range(c, ncol))])
            for i, (rr, cc) in enumerate(zip(range(r, nrow), range(c, ncol))):
                mat[rr][cc] = numbers[i]
        for r in range(nrow): sort_diagonal(r, 0)
        for c in range(1, ncol): sort_diagonal(0, c)
        return mat            
