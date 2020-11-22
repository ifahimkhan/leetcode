class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str, k: int = 2) -> int:
        n, max_length, memo = len(s), 0, defaultdict(int)
        
        left, right = 0, 0
        while left < n:
            while right < n and not (s[right] not in memo and len(memo) == k):
                memo[s[right]] += 1
                right += 1
        
            max_length = max(max_length, sum(memo.values()))
            memo[s[left]] -= 1
            if memo[s[left]] == 0: memo.pop(s[left])
            left += 1
            
        return max_length
