class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) {
        vector<int> squares(A.begin(), A.end());
        int l=0,r=A.size()-1,k=A.size()-1;
        while (l < r) {
            if (abs(A[l]) > abs(A[r])) squares[k--] = A[l] * A[l++];
            else squares[k--] = A[r] * A[r--];
        }
        squares[k] = A[l] * A[l];
        return squares;
    }
};
