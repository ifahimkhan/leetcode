// [7,2,5,10,8] m = 2
// first subarrays                          second subarrays
// [7,2,5,10]                               [8]
//      24                                   8
//                     max(24, 8) = 24
// [7,2,5]                                  [10,8]
//      14                                   18
//                     max(14, 18) = 18
// [7,2]                                    [5,10,8]
//       9                                   23
//                     max(9, 23)  = 23
// [7]                                      [2,5,10,8]
//       7                                   25
//                     max(7, 25)  = 25
//          min({24, 18, 23, 25}) = 18
    
// [7,2,5,10,8] m = 3            
//                          split by k
// first second subarrays       |           third subarrays
// [7,2,5,10]                               [8]    
// [7][2,5,10] [7,2][5,10] [7,2,5][10]    
//  7   17       9    15      14   10
//    17            15           14
//             14                           8
//                          max(14, 8) = 14
// first second subarrays       |           third subarrays
// [7,2,5]                                  [10,8]    
//     7                                      18
//                          max(7, 18) = 18
// first second subarrays       |           third subarrays
// [7,2]                                    [5,10,8]        
//     7                                      23
//                          max(7, 23) = 23

// f(i,j) = min( max subarray sums when splitting nums[:j) into i groups)
// the question is asking f(m,nums.size())
// basecase f(i,j) = sum(nums[:j)) if i == 1
// f(i,j) = min( max(f(i-1,k), sum(nums[k:j])) for k in ... )                         

class Solution {
public:
    int splitArray(vector<int>& nums, int m) {
        int n=nums.size();
        vector<long> accum,dp,ndp; // O(3n) space
        accum.push_back(nums[0]);
        for (int i=1;i<n;i++) accum.push_back(accum.back() + nums[i]);
        dp = accum;
        for (int i=1;i<m;i++) { // O(m) time
            ndp = vector<long>(n, INT_MAX);
            for (int j=0;j<n;j++) {  // O(n) time
                for (int k=0;k<j;k++){  // O(n) time
                    ndp[j] = min(
                        ndp[j],
                        max(dp[k], accum[j]-accum[k])
                    );
                }
            }
            dp = ndp;
        }
        return dp[n-1];
    }
};