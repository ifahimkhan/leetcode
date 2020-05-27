//  [[1,2],[2,3],[3,4],[4,5],[1,5]]
 

// party 0    party 1
//   1           2
//   3           4
//   5           1
    


class Solution {
public:
    bool possibleBipartition(int N, vector<vector<int>>& dislikes) {
        // convert edge list to adj_list
        // O(E) in space and time
        vector<vector<int>> adj_lists(N+1);
        for (auto p:dislikes) { 
            adj_lists[p[0]].push_back(p[1]);
            adj_lists[p[1]].push_back(p[0]);
        }
        
        // party assignments, component by component
        // O(N+E) in time O(N) in space
        unordered_map<int, int> party;
        for (int i=1;i<=N;i++) {
            if (party.count(i)) continue;
            party[i] = 0;
            deque<int> tour={i};
            while (not tour.empty()) {
                int a = tour.front(); tour.pop_front();
                for (int b:adj_lists[a]) {
                    if (not party.count(b)) {
                        party[b] = 1 ^ party[a];
                        tour.push_back(b);
                    }
                    if (party[b] == party[a]) return false;
                }
            }
        }
        return true;
    }
};