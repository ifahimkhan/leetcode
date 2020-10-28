class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        stack = []
        for num in nums:
            if not stack or (num > stack[-1][-1] + 1): 
                stack.append([num, num])
            stack[-1][-1] = num
        
        def format_range(_range):
            l, r = _range
            return str(l) if l == r else '{}->{}'.format(l, r)
        
        return list(map(format_range, stack))
