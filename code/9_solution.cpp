class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0 or (x % 10 == 0 and x)) return false;
        int rx = 0;
        while (x > rx) {
            rx = 10 * rx + x % 10;
            x /= 10;
        }
        return x == rx or x == rx / 10;
    }
};
