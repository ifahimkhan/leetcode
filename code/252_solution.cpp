class Solution {
public:
    bool canAttendMeetings(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(),
            [](auto a, auto b) {return a[0] < b[0];});
        
        int prev_end = INT_MIN;
        for (auto itv:intervals) {
            if (itv[0] < prev_end) return false;
            prev_end = itv[1];
        }
        return true;
    }
};