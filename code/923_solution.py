MOD = 10**9 + 7


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        freq_counts = Counter(arr)
        nums = sorted(list(freq_counts.keys()))
        n = len(nums)
        total = 0
        
        for i, num1 in enumerate(nums):
            c1 = freq_counts[num1]
            
            if 3 * num1 == target: 
                total += c1 * (c1 - 1) * (c1 - 2) // 6
            
            
            for j, num2 in enumerate(nums[i+1:]):
                num3 = target - num1 - num2
                c2, c3 = freq_counts[num2], freq_counts[num3]
                
                if num1 * 2 + num2 == target:
                    total += c1 * (c1 - 1) * c2 // 2
                
                if num1 + 2 * num2 == target:
                    total += c1 * c2 * (c2 - 1) // 2
                
                if num3 > num2 and num1 + num2 + num3 == target:
                    total += c1 * c2 * c3
                    
                    
        return total % MOD
