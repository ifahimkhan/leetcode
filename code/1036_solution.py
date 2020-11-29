class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set()
        stack = [start]
        while stack:
            loc = stack.pop(0)
            visited.add(loc)
            if arr[loc] == 0: return True
            left, right = loc - arr[loc], loc + arr[loc]
            for loc in [left, right]:
                if 0 <= loc < n and loc not in visited:
                    stack.append(loc)
        return False
