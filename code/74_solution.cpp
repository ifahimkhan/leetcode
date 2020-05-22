class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (not matrix.size() or not matrix[0].size()) return false;
        
        int nrow=matrix.size(), ncol=matrix[0].size();
        int l=0,h=nrow*ncol-1,m,r,c;
        while (l <= h) {
            m = l + (h - l) / 2;
            r = m / ncol;
            c = m % ncol;
            if (matrix[r][c] == target) return true;
            else if (matrix[r][c] > target) h = m - 1;
            else l = m + 1;
        }
        return false;
    }
};