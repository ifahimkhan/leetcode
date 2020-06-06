class UnionFind {
public:
    vector<int> parents;
    vector<int> sizes;
    int n_components;

    UnionFind(int n) {
        for (int i=0;i<n;i++) {
            parents.push_back(i);
            sizes.push_back(1);
        }
        n_components = n;
    }
    
    int find_set(int i) {
        while (i != parents[i]) {
            parents[i] = find_set(parents[i]);
            i = parents[i];
        }
        return i;
    }
    
    void union_set(int p, int q) {
        int root_p = find_set(p), root_q = find_set(q);
        if (root_p == root_q) return;
        int small = sizes[root_p] < sizes[root_q] ? root_p : root_q;
        int big = sizes[root_p] < sizes[root_q] ? root_q : root_p;
        parents[small] = big;
        sizes[big] += sizes[small];
        --n_components;
    }
};


class Solution {
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        UnionFind uf{n};
        for (auto& edge:edges) {
            uf.union_set(edge[0], edge[1]);
        };
        return uf.n_components;
    }
};