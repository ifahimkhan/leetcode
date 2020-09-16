class Solution(object):
    def findMaximumXOR(self, nums):
        answer = 0
        for i in reversed(range(32)):
            answer <<= 1
            prefixes = set(num >> i for num in nums)
            answer += any(answer ^ 1 ^ p in prefixes for p in prefixes)
        return answer
