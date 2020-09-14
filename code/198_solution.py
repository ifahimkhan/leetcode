class Solution:
    def rob(self, nums: List[int]) -> int:
        ready, today = 0, 0
        for num in nums:
                        # rest today # rob_today vs rest today 
            ready, today = today, max(ready + num, today)
        return today
                        
