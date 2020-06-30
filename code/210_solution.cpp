class Solution {
public:
    vector<int> findOrder(int N, vector<vector<int>>& prerequisites) {
        bool taken[100000]={false}, path[100000]={false};  // O(N)
        // graph processing  edge list -> adj list
        vector<vector<int>> next_courses(N);
        for (auto t:prerequisites) next_courses[t[1]].push_back(t[0]); // O(E), O(E)
        vector<int> order;
        // dfs function return cycle or not
        function<bool(int)> dfs = [&](int c) {
            if (taken[c]) return false;
            if (path[c]) return true;
            path[c] = true;
            
            for (int next:next_courses[c]) {
                bool has_cycle = dfs(next);
                if (has_cycle) return true;
            }
            taken[c] = true;
            path[c] = false;
            order.push_back(c);
            return false;
        };
        
        // try dfs search to detect cycle
        for (int c=0;c<N;c++) {  // O(N) time
            if (taken[c]) continue;
            if (dfs(c)) return {};  // O(E) time
        };
        
        reverse(order.begin(), order.end());
        return order;        
    }
};