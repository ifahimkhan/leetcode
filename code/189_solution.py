class Solution:
    # from nums = 1, 2, 3, 4, 5, 6   k = 2 
    # to          5, 6, 1, 2, 3, 4
    
    def solution_reverse(self, nums, k):
        # 1 2 3 4 5 6
        # 6 5 4 3 2 1  reverse all
        # 5 6 4 3 2 1  reverse up to k
        # 5 6 1 2 3 4  revsere from k + 1 to end
        
        def reverse_section(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        n = len(nums)
        k = k % n
        reverse_section(nums, 0, n - 1)
        reverse_section(nums, 0, k - 1)
        reverse_section(nums, k, n - 1)

    def solution_cycle(self, nums, k):
        # 1 2 3 4 5 6
        
        # 1 2 1 4 5 6   current = 2 tmp = 3  
        # 1 2 1 4 3 6   current = 4 tmp = 5
        # 5 2 1 4 3 6   current = 0 tmp = 1 
        
        # 5 2 1 2 3 6
        # 5 2 1 2 3 4
        # 5 6 1 2 3 4
        
        n = len(nums)
        k %= n
        
        start, count = 0, 0
        while count < n:
            current, tmp = start, nums[start]
            while True: 
                next_ = (current + k) % n
                nums[next_], tmp = tmp, nums[next_]
                current = next_
                count += 1
                if current == start:
                    break
            start += 1
    
    rotate = solution_cycle # solution_reverse
