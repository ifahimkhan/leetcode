
#  1 3 3 4 5
# [1,2,2,3,4]
 
#  1 2    5  6
# [2,3,4,4,4,5]

#  0 1 2 3 4
# [1,2,3,4,4,5]

#  0 1 2 3 4
# [1,2,3,2,4]

# 0->1->2->3->3

#  0 1 2 3 4 5
# [2,3,4,4,4,5]

# 0->2->4->4

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
#         l, h = 1, len(nums) - 1
#         while l < h:
#             m = (l + h) // 2
#             count = sum(num <= m for num in nums)
#             if count <= m: l = m + 1
#             else: h = m
#         return l

        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
