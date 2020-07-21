class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int count=0, max_len = 0;
        for (const int num: nums) {
            if (num) max_len = max(max_len, ++count);
            else count = 0;
        }
        return max_len;
    }
};