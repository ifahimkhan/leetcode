class Solution:
    def findLHS(self, nums: List[int]) -> int:
        num_freq = Counter(nums)
        max_length = 0
        for num, freq in num_freq.items():
            if num + 1 not in num_freq: continue
            max_length = max(max_length, freq + num_freq[num + 1])
        return max_length
