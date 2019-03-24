class Codec:
    def __init__(self):
        self.dic = {}
        self.counter = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl not in self.dic:
            shortUrl="http://tinyurl.com/{}".format(str(self.counter))
            self.dic[longUrl] = shortUrl
            self.dic[shortUrl] = longUrl
            self.counter +=1
            return shortUrl
        else:
            self.dic[longUrl]
        
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.dic[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))