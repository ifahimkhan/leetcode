class Solution {
public:
    double myPow(double x, int n) {
        long N = (long)n;
        if (N < 0) {
            x = 1 / x;
            N = -N;
        }
        double accum = 1;
        while (N) {
            if (N & 1) accum *= x;
            x *= x;
            N >>= 1;
        }
        return accum;
    }
};