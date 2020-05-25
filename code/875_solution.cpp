class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int H) {
        auto ceil_div = [](int x, int y) {return x % y ? x / y + 1 : x / y;};
        
        int l= ceil_div(*min_element(piles.begin(), piles.end()), H);
        int h= *max_element(piles.begin(), piles.end());
        
        auto criterion = [&](int target){
            int total = 0;
            for (auto pile:piles) total += ceil_div(pile, target);
            return total > H;
        };
        
        while (l < h) {
            int m = l + (h - l) / 2;
            if (criterion(m)) l = m + 1;
            else h = m;
        }
        return l;
    }
};