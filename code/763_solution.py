class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_pos = {char:idx for idx, char in enumerate(S)}
        head, tail = 0, 0
        partitions = []
        for idx, char in enumerate(S):
            tail = max(tail, last_pos[char])
            if idx == tail:
                partitions.append(idx - head + 1)
                head = idx + 1
        return partitions
