class Solution {
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        vector<int> weakest_rows;
        int nrow=mat.size(), ncol=mat[0].size();
        int c,r;
        for (c=0;c<ncol and k;c++){
            for (r=0;r<nrow and k;r++){
                if (mat[r][c]) continue;
                if (c and not mat[r][c-1]) continue;
                weakest_rows.push_back(r);
                k--;
            }
        }
        for (r=0;r<nrow and k;r++) {
            if (not mat[r][ncol-1]) continue;
            weakest_rows.push_back(r);
            k--;
        }
        return weakest_rows;
    }
};