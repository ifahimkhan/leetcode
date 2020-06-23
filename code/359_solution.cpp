class Logger {
private:
    unordered_map<string, int> memo;
public:
    /** Initialize your data structure here. */
    Logger() { memo = {}; }
    
    /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity. */
    bool shouldPrintMessage(int timestamp, string message) {
        if (not memo.count(message) or timestamp - 10 >= memo[message]){
            memo[message] = timestamp;
            return true;
        }
        return false;
    }
};

/**
 * Your Logger object will be instantiated and called as such:
 * Logger* obj = new Logger();
 * bool param_1 = obj->shouldPrintMessage(timestamp,message);
 */