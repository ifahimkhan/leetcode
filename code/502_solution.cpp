typedef pair<int, int> ii;
class cmp {
public:
    bool operator()(ii a, ii b) {
        return a.first > b.first;
    }
};


class Solution {
public:
    int findMaximizedCapital(int k, int W, vector<int>& Profits, vector<int>& Capital) {
        int n = Profits.size();
        vector<ii> projects;
        for (int i=0;i<n;++i) projects.push_back({Capital[i], Profits[i]});
        priority_queue<ii, vector<ii>, cmp> projects_pq{cmp{}, projects};
        priority_queue<int> feasible;
        
        while (k--) {
            while (not projects_pq.empty() and projects_pq.top().first <= W) {
                feasible.push(projects_pq.top().second);
                projects_pq.pop();
            }
            if (feasible.empty()) return W;
            W += feasible.top();
            feasible.pop();
        }
        return W;
    }
};