class UnionFind {
public:
    vector<int> parents;
    vector<int> sizes;

    UnionFind(int n) {
        for (int i=0;i<n;i++) {
            parents.push_back(i);
            sizes.push_back(1);
        }
    }
    
    int find_set(int i) {
        while (i != parents[i]) {
            parents[i] = find_set(parents[i]);
            i = parents[i];
        }
        return i;
    }
    
    bool union_set(int p, int q) {
        int root_p = find_set(p), root_q = find_set(q);
        if (root_p == root_q) return false;
        int small = sizes[root_p] < sizes[root_q] ? root_p : root_q;
        int big = sizes[root_p] < sizes[root_q] ? root_q : root_p;
        parents[small] = big;
        sizes[big] += sizes[small];
        return true;
    }
};


class Solution {
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size() + 1;
        UnionFind uf{n};
        for (auto edge:edges) {
            if (not uf.union_set(edge[0], edge[1])) return edge;
        };
        return {-1,-1};
    }
};