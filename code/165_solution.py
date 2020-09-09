class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        n1, n2 = len(version1), len(version2)

        def get_next(s, l):
            ''' get next digit from s, starting from index l'''
            num = 0
            while l < len(s) and s[l] != '.':
                num = 10 * num + int(s[l])
                l += 1
            return num, l + 1

        
        i, j = 0, 0
        # compare section by section
        while i < n1 and j < n2:
            v1, i = get_next(version1, i)
            v2, j = get_next(version2, j)
            if v1 > v2: return 1
            if v1 < v2: return -1
        
        # both exhausted tire
        if i == n1 + 1 and j == n2 + 1: return 0
        
        # version 1 exhausted, check if remainder of version 2 are all 0
        if i == n1 + 1:
            for k in range(j, n2): 
                if version2[k] not in ['.', '0']: return -1 

        # version 2 exhausted, check if remainder of version 1 are all 0
        if j == n2 + 1:
            for k in range(i, n1):
                if version1[k] not in ['.', '0']: return 1        
        return 0
