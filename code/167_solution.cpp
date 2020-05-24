class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l=0,r=numbers.size()-1;
        while (l < r) {
            int two_sum = numbers[l] + numbers[r];
            if (two_sum == target) return {l+1,r+1};
            if (two_sum > target) r--;
            else l++;
        }
        return {-1,-1};
    }
};