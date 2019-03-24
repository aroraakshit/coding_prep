from collections import defaultdict
class moddict(dict):
    def __missing__(self, key):
        return -1
    
class Logger: # 96ms

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = moddict()

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if self.d[message]==-1 or timestamp - self.d[message] >= 10:
            self.d[message] = timestamp
            return True
        return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)