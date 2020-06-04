class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int max = *max_element(candies.begin(), candies.end());
        vector<bool> possible;
        for (const int x:candies) possible.push_back((bool)(x + extraCandies >=max));
        return possible;
    }
};