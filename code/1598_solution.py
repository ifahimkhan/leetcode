class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for action in logs:
            if action == './': continue
            elif action == '../': depth -= 1 if depth else 0
            else: depth += 1
        return depth
