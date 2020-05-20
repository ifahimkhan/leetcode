class Solution {
private:
    int binary_search_left(vector<int>& nums, int target) {
        int l=0, h=nums.size(), m;
        while (l < h) {
            m = l + (h - l) / 2;
            if (nums[m] < target) l = m + 1;
            else h = m;
        }
        return l;
    }
    int binary_search_right(vector<int>& nums, int target) {
        int l=0, h=nums.size(), m;
        while (l < h) {
            m = l + (h - l) / 2;
            if (nums[m] <= target) l = m + 1;
            else h = m;
        }
        return l-1;
    }    
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int l = binary_search_left(nums, target);
        int r = binary_search_right(nums, target);
        return (r >= l) ? vector<int>{l,r} : vector<int>{-1,-1};
    }
};