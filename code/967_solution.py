class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        if N == 1: return list(range(10))
        queue = deque(range(1, 10))
        for _ in range(N-1):
            for _ in range(len(queue)):
                num = queue.popleft()
                last = num % 10
                for next_ in set([last + K, last - K]):
                    if next_ >= 10 or next_ < 0: continue
                    queue.append(num * 10 + next_)
        return queue
