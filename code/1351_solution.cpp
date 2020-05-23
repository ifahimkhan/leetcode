class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int nrow = grid.size(), ncol = grid[0].size();
        int r = 0, c = ncol - 1;
        int total = 0;
        while (r < nrow and c >= 0) {
            if (grid[r][c] < 0) {
                total += nrow - r;
                c--;
            } else r++;
        }
        return total;
    }
};