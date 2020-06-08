class UnionFind {
public:
    vector<int> parents;
    vector<int> sizes;
    int n_components;

    UnionFind(int n) {
        make_set(n);
    }

    void make_set(int n) {
        parents.resize(n);
        sizes.resize(n);
        for (int i=0;i<n;i++) {
            parents[i] = i;
            sizes[i] = 1;
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
private: 
    bool similar(string_view w1, string_view w2) {
        for (int i=0,diff=0;i<w1.size();i++) {
            if (w1[i] != w2[i] and ++diff > 2) return false;
        }
        return true;
    }
public:
    int numSimilarGroups(vector<string>& A) {
        int N = A.size(), W = A[0].size();
        UnionFind uf{N};
        
        if (N < W * W) {
            for (int i=0;i<N;i++) {
                for (int j=i+1;j<N;j++) {
                    if (similar(A[i], A[j])) uf.union_set(i, j);
                }
            }
        } else {
            unordered_map<string, unordered_set<int>> sim_with;
            for (int i=0;i<N;i++) {
                string w = A[i];
                for (int j=0;j<W;j++) {
                    for (int k=j+1;k<W;k++) {
                        swap(w[j], w[k]);
                        sim_with[w].insert(i);
                        swap(w[j], w[k]);
                    }
                }
            }
  
            for (int i=0;i<N;i++) {
                for (auto j:sim_with[A[i]]) {
                    if (i == j) continue;
                    uf.union_set(i, j);
                }
            }
        }

        return uf.n_components;
    }
};