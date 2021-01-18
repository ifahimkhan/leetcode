class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq_counts = Counter(nums)
        total = 0
        for num, freq in freq_counts.items():
            if num * 2 == k:
                total += freq // 2
            elif num <= k // 2 and k - num in freq_counts:
                total += min(freq, freq_counts[k - num])
        return total
