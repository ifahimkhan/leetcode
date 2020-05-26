//     i = 2
// A 1 4 2 3
//   |  \
// B 1 2 4 3
//       j = 3
// f(1,1) = 1
// f(1,2) = 1
// f(2,1) = 1
// f(2,2) = 1
// f(2,3) = 2    
// f(3,2) = 2
// f(3,3) =max of  f(2,3),  // choose not to use A[3]  2 
//                 f(3,2),  // choose not to use B[3]  2
//                 f(2,2) + (int)(A[3] == B[3])     // 1
// f(3,4) = max(f(2,4), f(3,3), f(2,3)) = 2        
//                  2     2        2                    
        
// f(i,j) = max uncrossed lines between A[0:i) and B[0:j)
// f(A.size(), B.size())
// basecase = 0
// f(i,j) = max(f(i-1,j), f(i,j-1), f(i-1,j-1) + (int)A[i-1][j-1])                                       
                                                  
// f(i,j)                                                  
//          j                                                  
//          0 1 2 3
//      i 0 0 0 0 0
//        1 0 1 1 1
//        2 0 1 1 2
//        3 0      
//                  x

class Solution {
public:
    int maxUncrossedLines(vector<int>& A, vector<int>& B) {
        int nrow=A.size()+1, ncol=B.size()+1;
        vector<int> prev(ncol, 0), curr;
        for (int r=1;r<nrow;r++) {
            curr = prev;
            for (int c=1;c<ncol;c++) {
                curr[c] = max({
                   prev[c],
                   curr[c-1],
                   prev[c-1] + (int)(A[r-1] == B[c-1]) 
                });
            }
            prev = curr;
        }
        return curr.back();
    }
};