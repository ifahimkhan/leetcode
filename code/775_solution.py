# global inversion is also local inversion
# so to have the two equal, we are only allowed to have local inversion of size 1

class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        for i, x in enumerate(A):
            if i - 1 <= x <= i + 1: continue
            return False
        return True
