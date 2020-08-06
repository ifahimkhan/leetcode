class Solution {
public:
    bool isPowerOfFour(int num) {
        if (num==INT_MIN) return false;
        return ((num & (num-1)) == 0) and (num % 3 == 1);
    }
};