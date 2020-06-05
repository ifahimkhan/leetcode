class Solution {
public:
    int findNumbers(vector<int>& nums) {
        auto evenDigits = [](int num) {
            int i = 0;
            while (num) {
                num /= 10;
                ++i;
            }
            return i & 1 ? 0 : 1;
        };
        int count=0;
        for (int num:nums) count += evenDigits(num);
        return count;
    }
};