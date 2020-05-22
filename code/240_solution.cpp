class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (not matrix.size() or not matrix[0].size()) return false;
        int nrow=matrix.size(), ncol=matrix[0].size();
        int r=0,c=ncol-1;
        while (r < nrow and c >= 0){
            if (matrix[r][c] == target) return true;
            else if (matrix[r][c] < target) r++;
            else c--;
        }
        return false;
    }
};
