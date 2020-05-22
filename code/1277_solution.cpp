// [1,1,1]  1+1+1  3
// [1,2,2]  1+2+2  3+5
// [1,2,3]  1+2+3  3+5+6 = 14

// f(r,c) = # square submatrices which has a bottom right location at (r,c)
// want sum(f(r,c) for r in .. for in ..)    

//    0
//     11?
//     12?    
//     ?21 <- r,c
    
   
// base case: 
// f(r,c) = matrix[r,c] if r == 0 or c == 0    
// f(r, c) = min(f(r-1, c-1), f(r, c-1), f(r-1, c))  + 1    

class Solution {
public:
    int countSquares(vector<vector<int>>& matrix) {
        vector<int> prev=matrix[0], curr=matrix[0];
        int total = accumulate(prev.begin(), prev.end(), 0);
        for (int r=1;r<matrix.size();r++) {
            for (int c=0;c<prev.size();c++) {
                if (matrix[r][c]==0) curr[c]=0;
                else if (c==0) curr[c]=1;
                else curr[c]=min({prev[r-1,c-1], curr[r,c-1], prev[r-1,c]})+1;
            }
            prev = curr;
            total += accumulate(prev.begin(), prev.end(), 0);
        }
        return total;
    }
};














