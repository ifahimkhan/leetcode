class Solution {
public:
    int mySqrt(int x) {
        if (x < 2) return x;
        long l=0, h=x, m;
        while (l < h) {
            m = l + (h - l) / 2;
            if (m * m <= x) l = m + 1;
            else h = m;
        }
        return l - 1;
    }
};