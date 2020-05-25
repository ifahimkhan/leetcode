class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int> tails;
        for (int num:nums) {
            auto loc = lower_bound(tails.begin(), tails.end(), num);
            if (loc == tails.end()) tails.push_back(num);
            else *loc = num;
        }
        return tails.size();
    }
};