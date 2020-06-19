# [0,1,3,5,6] N = 5, h = 3


# [0, 1] 3 [3, 5, 6] len = 3 min = 3

# [0,1,3,5,6]
#          ^
#          1 < 6

# [0,1,3,5,6]
#        ^
#        2 < 5

# [0,1,3,5,6]
#      ^
#      3 == 3 
        
# [0,1,3,5,6]
#    ^
#    4 > 1
        
#  0 1 2 3 4
# [0,1,3,5,6]
#      ^
#      i = 2      
#      3 == 3    
#   N - i <= citations[i]

# handle special case when citations[-1] = 0 or no paper
# No citation no h index

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations or citations[-1] == 0: return 0
        N = len(citations)
        l, h = 0, N - 1
        while l < h:
            i = (l + h) // 2
            if N - i > citations[i]: l = i + 1
            else: h = i
        return N - l 
