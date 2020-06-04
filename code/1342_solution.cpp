class Solution {
public:
    int numberOfSteps (int num) {
        int steps = 0;
        while (num) {
            num -= num & 1 ? 1 : num >> 1;
            ++steps;
        }
        return steps;
    }
};