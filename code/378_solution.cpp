class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int l=matrix.front().front(), h=matrix.back().back();
        
        auto criterion = [&](int t) {
            int total = 0;
            for (auto row:matrix) {
                total += upper_bound(row.begin(), row.end(), t) - row.begin();
            }
            return total < k;
        };
        while (l < h) {
            int m = l + (h - l) / 2;
            if (criterion(m)) l = m + 1;
            else h = m;
        }
        return l;
    }
};