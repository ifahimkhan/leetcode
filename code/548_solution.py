# # for i in 
# #     for j in 
# #         if sum(0, i-1) == sum(i+1,j-1):
# #             for k in 
# #    i       j
# # 40000000004x            

# for j in range
    
#     for i in 
#         if sum(0, i-1) == sum(i+1,j-1):
#             save the sum in a set
#     for k in 
#         if sum(j+1, k-1) == sum(k+1, n-1) == one of the sum from the set
#             return True
 
# n = 7
#  0 1 2 3 4 5 6   
# [1,2,1,2,1,2,1]
#    i   j   k
  
class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        # get prefix sum
        n = len(nums)
        accum = [nums[0]]
        for num in nums[1:]: accum.append(accum[-1] + num)
            
        for j in range(3, n-3): # exploring mid point
            targets = set()
            for i in range(1, j-1): # grouping
                sum_l1 = accum[i-1]
                sum_l2 = accum[j-1] - accum[i]
                if sum_l1 == sum_l2: targets.add(sum_l1)
            for k in range(j+2,n-1): # checking
                sum_r1 = accum[k-1] - accum[j]
                sum_r2 = accum[n-1] - accum[k]
                if sum_r1 == sum_r2 and sum_r1 in targets: return True
        return False
