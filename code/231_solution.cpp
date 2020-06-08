//   8421
// 0b1101 -> 1*1+0*2+1*4+1*8 = 13
//  x      0100 
//  x - 1  0011
// &-------------
//         0000

class Solution {
public:
    bool isPowerOfTwo(int n) {
        return (n > 0 and (n & n - 1) == 0);
    }
};