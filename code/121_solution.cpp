class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int prev_min = INT_MAX, max_profit = 0;
        for (const int p:prices) {
            prev_min = min(p, prev_min);
            max_profit = max(max_profit, p - prev_min);
        }
        return max_profit;
    }
};