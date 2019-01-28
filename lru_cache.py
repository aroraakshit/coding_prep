class LRUCache: # 3 seconds, faster than only 1% solutions

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # print("get", key, self.cache)
        i = len(self.cache)
        value = None
        for k in range(len(self.cache)):
            if key in self.cache[k]:
                i = k
                value = self.cache[k][key]
                break
        
        if i < len(self.cache): # found
            del self.cache[i]
            self.cache.append({key:value})
            return self.cache[-1][key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # print("put", key, value, self.cache)
        i = len(self.cache)
        for k in range(len(self.cache)):
            if key in self.cache[k]:
                del self.cache[k]
                self.cache.append({key:value})
                i = k
                break
        
        if i == len(self.cache): # unsuccessful search
            if len(self.cache) < self.capacity: 
                self.cache.append({key:value})
            else:
                del self.cache[0]
                self.cache.append({key:value})


class LRUCache: # 576ms, faster than only 13% solutions

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}
        self.recent = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # print("get", key, self.cache)
        if key in self.cache:
            self.recent += 1
            self.cache[key][1] = self.recent
            return self.cache[key][0]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # print("put", key, value, self.cache)
        if key in self.cache:
            self.cache[key][0] = value
        else:
            if len(self.cache) == self.capacity:
                # remove the least recently used cache
                mini = self.recent+1
                minkey = mini
                for i in self.cache.keys():
                    if self.cache[i][1] < mini:
                        minkey = i
                        mini = self.cache[i][1]
                del self.cache[minkey]
            self.cache[key] = [value,-1]
            
        self.recent = (1 + self.recent)
        self.cache[key][1] = self.recent
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


class LRUCache(dict): # 96ms solution, credits: LeetCode

    def __init__(self, capacity):
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return -1
        
        val = self.pop(key)
        self[key] = val
        return val

    def put(self, key, value):
        if key in self:
            self.pop(key)
            
        if len(self) == self.capacity:
            self.pop(next(iter(self)))
            
        self[key] = value