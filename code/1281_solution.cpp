class Solution {
public:
    int subtractProductAndSum(int n) {
        int accum_prod = 1, accum_sum = 0;
        while (n) {
            int d = n % 10;
            n /= 10;
            accum_prod *= d;
            accum_sum += d;
        }
        return accum_prod - accum_sum;
    }
};