// f(i) = abs(arr[i] - x)   vs i
// g(i) = f(i) <= f(i+k)  
    
//   k == 5
 
//  00 1 11111  
// f(i)
// ^*               *
// | *            *
// | |*_________*
// |          *|
// |    *   *
// |      *
// ------------------> i
class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int l=0, h=arr.size()-k,m;  
        while (l < h) {
            m = l + (h - l) / 2; // m is the starting index for window of size k
            if (x - arr[m] > arr[m+k] - x) l = m + 1;
            else h = m;
        }
        return vector<int>(arr.begin()+l,arr.begin()+l+k);
    }
};