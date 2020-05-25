// [1 2 3 4 5 | 6 7 8 9 10] median = (5+6)/2 = 5.5
//        5        5
     
// nums1[:3)  nums1[3:]   
//       p1=3 
// [1 3 5 | 7 9]  
//      p2=2 =  half(5) - p1
// [2 4 | 6 8 10]   
// noticed that max_left <= min_rigt

//  case 1
//       p1=2 
// [1 3 | 5 7 9]  
//         p3=3
// [2 4 6 | 8 10]   
// max_left 6 > min_right 5  max_left_2 > min_right_1 increase lower bound
      
//  case 1
//       p1=4 
// [1 3 5 7 | 9]  
//   p2=1
// [2 | 4 6  8 10]  
// max_left 7 > min_right 4  max_left_1 > min_right_2 decrease upper bound  

// boundry case 
// p1=0 use INT_MIN as max_left_1      
// [|1 3 5 7 9]  
//   p2=5 == len(nums2) use INT_MAX         
// [2 4 6  8 10|]  

//          V  
// [1 2 3 4 5 6 7 8 9]  ceil(9 / 2)

// [2 4 | 6 8]   
// [1 3 5 | 7 9]  
// in odd case if we take ceil in half calculation, median is max_left
      
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) swap(nums1, nums2);
        int n1 = nums1.size(), n2 = nums2.size();
        int half = (n1 + n2 + 1) / 2;
        int is_odd = (n1 + n2) & 1;
        int l = 0, h = n1;
        while (l <= h) {
            int p1 = l + (h-l)/2, p2 = half - p1;
            int max_left_1 = p1 ? nums1[p1-1] : INT_MIN;
            int max_left_2 = p2 ? nums2[p2-1] : INT_MIN;
            int min_right_1 = p1 < n1 ? nums1[p1] : INT_MAX;
            int min_right_2 = p2 < n2 ? nums2[p2] : INT_MAX;
            int max_left = max(max_left_1, max_left_2);
            int min_right = min(min_right_1, min_right_2);
            if (max_left <= min_right) {
                if (is_odd) return max_left;
                else return (double)(min_right + max_left) / 2;
            } else if (max_left_2 > min_right_1) l = p1 + 1;
            else if (max_left_1 > min_right_2) h = p1 - 1;
        }
        return -1;
    }
};
