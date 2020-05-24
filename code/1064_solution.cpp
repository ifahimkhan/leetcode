class Solution {
public:
    int fixedPoint(vector<int>& A) {
        int l=0, h=A.size()-1, m;
        while (l < h) {
            m = l + (h - l) / 2;
            if (A[m] < m) l = m + 1;
            else h = m;
        }
        return A[l] == l ? l : -1;
    }
};