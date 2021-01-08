class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        i1 = i2 = c1 = c2 = 0
        n1, n2 = len(word1), len(word2)

        while i1 != n1 and i2 != n2:
            if word1[i1][c1] != word2[i2][c2]: 
                return False

            c1 += 1
            if c1 == len(word1[i1]):
                i1 += 1
                c1 = 0
            
            c2 += 1
            if c2 == len(word2[i2]):
                i2 += 1
                c2 = 0
            
            if i1 == n1 and i2 == n2:
                return True
        return False
