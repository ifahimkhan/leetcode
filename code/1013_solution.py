 # [0,2,1,-6,6,-7,9,1,2,0,1]  sum = 9
 #      i             j
 #    3      3           3

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        if total % 3: return False
        target = total // 3
        accum = counter = 0
        for num in A:
            if counter == 2: return True
            accum += num
            if accum == target:
                counter += 1
                accum = 0
        return False
