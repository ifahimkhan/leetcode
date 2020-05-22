// i  0 1 2
// w [1,2,3] total_weight = 1+2+3=6

// 1/6 chance to pick index 0
// 2/6 chance to pick index 1
// 3/6 chance to pick index 2
    
// roll a fair six face die

//  1 2 3 4 5 6
// [0 1 1 3 3 3]    

//  0  1  2  3
// [w1,w2,w3,w4]

// concate(duplicate(0, w1),duplicate(1, w2),duplicate(2, w3),duplicate(3, w4))

//  1|2 3|4 5 6  -> 1|3|6  accum weight
// [0|1 1|3 3 3]    0|1|3   

//                   4

class Solution {
private:
    vector<int> accum_w;
    int binary_search(int target) {
        int l=0, h=accum_w.size(), m;
        while (l < h) {
            m = l + (h - l) / 2;
            if (accum_w[m] < target) l = m + 1;
            else h = m;
        }
        return l;
    }
public:
    Solution(vector<int>& w) {
        int accum = 0;
        for (int weight:w) {
            accum += weight;
            accum_w.push_back(accum);
        }
    }
    
    int pickIndex() {
        int rn = rand() % accum_w.back() + 1;
        return binary_search(rn);
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(w);
 * int param_1 = obj->pickIndex();
 */