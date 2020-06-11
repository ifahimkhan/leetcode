class Solution {
public:
    void sortColors(vector<int>& nums) {
        int l=0, r=nums.size()-1, m=0;
        while (m <= r) {
            if (nums[m] == 0) {
                swap(nums[m], nums[l]);
                ++l;
                ++m;
            } else if (nums[m] == 2) {
                swap(nums[m], nums[r]);
                --r;
            } else ++m;
        }
    }
};