// queue + set, slower on single check, but only keeps 10 seconds of data at any given moment.
class Logger {
private:
    queue<pair<string, int>> msg_queue;
    unordered_set<string> messages;
public:
    /** Initialize your data structure here. */
    Logger() { msg_queue = {}; messages = {};}
    
    /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity. */
    bool shouldPrintMessage(int timestamp, string message) {
        while (not msg_queue.empty() and msg_queue.front().second <= timestamp - 10) {
            messages.erase(msg_queue.front().first);
            msg_queue.pop();
        }
        if (not messages.count(message)) {
            msg_queue.push({message, timestamp});
            messages.insert(message);
            return true;
        };
        return false;

    }
};


// map solution, faster but more memory hungry through time. because, it keeps everything.

class Logger {
private:
    unordered_set<string> memo;
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
