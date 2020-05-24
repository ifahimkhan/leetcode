class Solution {
public:
    bool isMajorityElement(vector<int>& nums, int target) {
        int l=0, h=nums.size()-1,m;
        while (l < h) {
            m = l + (h - l) / 2;
            if (nums[m] < target) l = m + 1;
            else h = m;
        }
        if (l >= nums.size() / 2) return false;
        return nums[l] == target and nums[l + nums.size()/2] == target;
    }
};