class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        # simulate bubble sort O(N^2)
        res = []
        for x in sorted(A, reverse=True):
            # at iteration j we flip the list to make (j+1)th largerst number to its rightful position
            i = A.index(x) 
            res.extend([i + 1, x])
            # A[:i:-1] is the reverse from back to number x
            # A[:i] is from front to number 
            # together it is to flip x to the end and update the new end to be the pos prior to x
            A = A[:i:-1] + A[:i]
        return res
