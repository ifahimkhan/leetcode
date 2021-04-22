class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        ends = defaultdict(int)
        for bricks in wall:
            loc = 0
            for brick in bricks[:-1]:
                loc += brick
                ends[loc] += 1
        return len(wall) if len(ends) == 0 else len(wall) - max(ends.values())
