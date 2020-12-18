class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        third = second = float('inf')
        for num in nums:
            if num > second: 
                return True
            if num < third: 
                third = num
            elif third < num < second: 
                second = num
        return False
