class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(),
            [](auto a, auto b) {return a[0] < b[0];});
            
        priority_queue<int, vector<int>, greater<int>> pq;
        for (auto itv:intervals) {
            if (not pq.empty() and itv[0] >= pq.top()) pq.pop();
            pq.push(itv[1]);
        }
        return pq.size();
    }
};