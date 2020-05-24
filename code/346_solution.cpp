class MovingAverage {
private:
    queue<int> numbers_;
    int max_size_,curr_size_;
    double total_;
public:
    /** Initialize your data structure here. */
    MovingAverage(int size) {
        numbers_ = {};
        max_size_ = size;
        curr_size_ = 0;
        total_ = 0;
    }
    
    double next(int val) {
        if (curr_size_ == max_size_) {
            total_ -= numbers_.front(); numbers_.pop();
            curr_size_--;
        }
        total_ += val;
        numbers_.push(val);
        curr_size_++;
        return total_ / curr_size_;        
    }
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage* obj = new MovingAverage(size);
 * double param_1 = obj->next(val);
 */
