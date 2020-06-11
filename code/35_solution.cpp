// find i such that  arr[:i] < target and arr[i:] >= target

class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int l=0, h=nums.size();
        while (l < h) {
            int m = l + (h - l) / 2;
            if (nums[m] < target) l = m+1;
            else h = m;
        }
        return l;
    }
};