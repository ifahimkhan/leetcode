class Solution {
public:
    int fib(int N) {
        if (N < 2) return N;
        int prev=0, curr=1, next;
        for (int i=2; i<=N; i++) {
            next = prev+curr;
            prev = curr;
            curr = next;
        }
        return curr;
    }
};
