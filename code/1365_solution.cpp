class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> sorted = nums, result;
        sort(sorted.begin(), sorted.end());
        unordered_map<int, int> num_smaller;
        int i = 0;
        for (int num:sorted) {
            if (not num_smaller.count(num)) num_smaller[num] = i;
            ++i;
        }
        for (int num:nums) result.push_back(num_smaller[num]);
        return result;
    }
};