class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> num_idx;
        for (int i=0;i<nums.size();i++) {
            int other = target - nums[i];
            if (num_idx.count(other)) return {i, num_idx[other]};
            num_idx[nums[i]] = i;
        }
        return {-1, -1};
    }
};
