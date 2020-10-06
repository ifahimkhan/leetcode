class Solution {
public:
    int connectSticks(vector<int>& sticks) {
        int total = 0;
        priority_queue<int, vector<int>, greater<int>> pq(sticks.begin(), sticks.end());
        while (pq.size() >= 2) {
            int l1 = pq.top(); pq.pop();
            int l2 = pq.top(); pq.pop();
            pq.push(l1 + l2);
            total += l1 + l2;
        }
        return total;
    }
};
