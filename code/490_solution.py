class Solution:
    def hasPath(self, maze, start, destination):
        queue = deque([start])
        nrow, ncol = len(maze), len(maze[0])
        dirs = ((0,-1),(0,1),(-1,0),(1,0))
        while queue:
            r, c = queue.popleft()
            if [r, c] == destination: return True
            for dr, dc in dirs:
                nr, nc = r, c
                while 0 <= nr + dr < nrow and 0 <= nc + dc < ncol and maze[nr + dr][nc + dc] != 1:
                    nr += dr
                    nc += dc
                if maze[nr][nc] == 0:
                    maze[nr][nc] = 2
                    queue.append([nr, nc])
        return False