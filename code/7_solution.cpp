class Solution {
public:
    int reverse(int x) {
        int rx=0;
        while (x){
            int d = x % 10;
            x /= 10;
            if (rx > INT_MAX / 10 or (rx == INT_MAX / 10 and d > 7)) return 0;
            if (rx < INT_MIN / 10 or (rx == INT_MIN / 10 and d < -8)) return 0;
            rx = 10 * rx + d;
        }
        return rx;
    }
};
