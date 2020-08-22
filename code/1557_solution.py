class Solution:
    def simulation(self, nums):
        total = 0
        n = len(nums)
        while True:
            for i in range(n):
                if nums[i] & 1:
                    total += 1
                    nums[i] -= 1
            if not sum(nums): 
                break
            else:
                nums = [num // 2 for num in nums]
                total += 1
        return total 

    def bitcount(self, nums):

        def _bitcount(num):
            num_bits, num_1_bits = 0, 0
            while num:
                num_bits += 1
                num_1_bits += num & 1
                num >>= 1
            return num_bits, num_1_bits
        
        total = 0
        max_bits = 0
        for num in nums:
            num_bits, num_1_bits = _bitcount(num)
            total += num_1_bits
            max_bits = max(max_bits, num_bits)

        return total + max_bits - 1

    minOperations = bitcount