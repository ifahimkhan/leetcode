class SummaryRanges {
private:
    vector<vector<int>> itvs_;
    void merge(int i){
        if (0 <= i and i < itvs_.size()-1){
            if (itvs_[i][1] + 1 >= itvs_[i+1][0]) {
                itvs_[i][1] = max(itvs_[i][1], itvs_[i+1][1]);
                itvs_.erase(itvs_.begin() + i + 1);
            }
        }
    }
public:
    /** Initialize your data structure here. */
    SummaryRanges() { itvs_ = {}; }
    
    void addNum(int val) {
        int l = 0, h = itvs_.size() - 1;
        while (l <= h) {
            int m = l + (h - l) / 2;
            if (itvs_[m][0] >= val) h = m - 1;
            else l = m + 1;
        }
        itvs_.insert(itvs_.begin() + l, {val, val});
        merge(l);
        merge(l-1);
    }
    
    vector<vector<int>> getIntervals() { return itvs_; }
};

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges* obj = new SummaryRanges();
 * obj->addNum(val);
 * vector<vector<int>> param_2 = obj->getIntervals();
 */