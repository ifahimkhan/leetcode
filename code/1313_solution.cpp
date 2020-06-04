class Solution {
public:
    vector<int> decompressRLElist(vector<int>& nums) {
        vector<int> decoded;
        for (int i=0; i<nums.size(); i+=2) {
            int repeat=nums[i], val=nums[i+1];
            while (repeat) {
                decoded.push_back(val);
                --repeat;
            }
        }
        return decoded;
    }
};