class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        taken = set()
        edge_list = defaultdict(set)
        n_prereqs = defaultdict(int)
        
        for pre, seq in relations:
            edge_list[pre].add(seq)
            n_prereqs[seq] += 1
        
        curr_semester = set(range(1, n + 1)) - set([seq for pre, seq in relations])
        if not curr_semester: return -1
        
        semester = 0
        while curr_semester:
            semester += 1
            next_semester = set()
            
            for course in curr_semester:
                if course in taken: return -1
                for seq in edge_list[course]:
                    n_prereqs[seq] -= 1
                    if n_prereqs[seq] == 0:
                        next_semester.add(seq)
            taken.update(curr_semester)
            curr_semester = next_semester
        return semester if len(taken) == n else -1
                
                
                
        
