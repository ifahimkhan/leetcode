class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited, stack = [], [0]
        while stack:
            room = stack.pop()
            if room not in visited:
                visited.append(room)
                stack.extend([key for key in rooms[room] if key not in visited])
        return len(visited) == len(rooms)
