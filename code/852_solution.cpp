//    V
//    -
//   -
//     -
//  -   -
// -     -
// 0123456
//    ^
//    i
// 0001111
// f(i) = (A[i] > A[i + 1])
       

class Solution {
public:
    int peakIndexInMountainArray(vector<int>& A) {
        int l=0, h=A.size()-1, m;
        while (l < h) {
            m = l + (h - l) / 2;
            if (A[m] > A[m + 1]) h = m;
            else l = m + 1;
        }
        return l;
    }
};