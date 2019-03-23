class LFUCache: # 128ms, faster than 91.73%, Credits - LeetCode

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.k = capacity
        self.cacheFreq = collections.defaultdict(collections.OrderedDict)
        self.cacheKey = {}
        self.leastFreq = 1
        
        
    def _update(self, key, new_v=None):
        freq, v = self.cacheKey[key]
            
        del self.cacheFreq[freq][key]
        if not self.cacheFreq[self.leastFreq]:
            self.leastFreq += 1 
            
        if new_v: v = new_v
        self.cacheFreq[freq+1][key] = v    
        self.cacheKey[key] = (freq + 1, v)    
        
        
    def _evict(self):
        key, _ = self.cacheFreq[self.leastFreq].popitem(last=False)
        del self.cacheKey[key]

        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cacheKey:
            return -1
        self._update(key)
        return self.cacheKey[key][1]
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cacheKey: 
            self._update(key, value)
            return
        
        self.cacheKey[key] = (1, value)
        self.cacheFreq[1][key] = value
        if self.k < len(self.cacheKey):
            self._evict()
        self.leastFreq = 1