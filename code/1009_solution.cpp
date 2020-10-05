class Solution {
public:
    int bitwiseComplement(int N) {
        int X = 1;
        while (N > X) X = X << 1 | 1;
        return X - N;
    }
};
