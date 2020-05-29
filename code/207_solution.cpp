//       5         ----->4
//       ^        /
//       |       /
//       V      /
// 0---->1---->2---->3

          
// taken = {3, 4, 2}
// path = [0, 1, 5, 1]
          
// dfs search
// when we want to push a course onto stack and found out its already on stack -> cycle 
// mark course as taken during backtrack.
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // graph processing
        vector<vector<int>> next_courses(numCourses);  // O(E) space
        for (auto t:prerequisites) next_courses[t[1]].push_back(t[0]); 
        
        bool taken[100000]={false}, path[100000]={false}; // O(V) space
        
        // return true if there is a cycle
        function<bool(int)> dfs = [&](int course) { 
            if (path[course]) return true;
            path[course] = true;
            
            for (int next:next_courses[course]) {
                bool has_cycle = dfs(next);
                if (has_cycle) return true;
            }
            path[course] = false;
            taken[course] = true;
            return false;
        };
        
        // dfs search for cycle detection
        for (int course=0;course<numCourses;course++) {
            if (taken[course]) continue;
            if (dfs(course)) return false;
        }
        return true;
    }
};