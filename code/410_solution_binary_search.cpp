// l = max(nums), h = sum(nums)

// [7,2,5,10,8] m = 2      17, 18, 19

// [7,2,5][10][8] needs 3  splits to have max(subarray sum) <= 17
// [7,2,5][10,8]  needs 2  splits to have max(subarray sum) <= 18
// [7,2,5][10,8]  needs 2  splits to have max(subarray sum) <= 19

// can_split(target) where target in [l,h]
// false, false, false, true, true
//                 17   18
    
class Solution {
public:
    int splitArray(vector<int>& nums, int m) {
        long l = *max_element(nums.begin(), nums.end()); 
        long h = accumulate(nums.begin(), nums.end(), (long)0);
        long mid;
        
        // O(N)
        auto num_splits = [&](long target) {
            long splits = 1, accum=0;
            for (int num:nums) {
                if (accum + num > target) {
                    splits++;
                    accum=0;
                }
                accum += num;
            }
            return splits;
        };
        
        // O(log(sum(nums) - max(nums)))
        while (l < h) {
            mid = l + (h - l) / 2;
            if (num_splits(mid) >= m) l = mid + 1;
            else h = mid;
        }
        cout << l << endl;
        return l;
    }
};