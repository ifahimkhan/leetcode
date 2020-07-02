class Solution:
    def findOrder(self, N: int, prerequisites: List[List[int]]) -> List[int]:
        # graph processing
        out_edges = [[] for _ in range(N)]
        in_degrees = [0 for _ in range(N)]
        for course, prereq in  prerequisites:
            out_edges[prereq].append(course)
            in_degrees[course] += 1
        
        # bfs search for feasibilty as well as order
        queue = [course for course, prereq in enumerate(in_degrees) if not prereq]
        queue = deque(queue)
        taken = []
        while queue:
            course = queue.popleft()
            taken.append(course)
            for next_course in out_edges[course]:
                in_degrees[next_course] -= 1
                if in_degrees[next_course] == 0: queue.append(next_course)
        return taken if len(taken) == N else []