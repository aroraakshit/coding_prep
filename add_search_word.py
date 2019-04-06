class TrieNode: 
    def __init__(self):
        self.end = False
        self.children = [None for i in range(26)]

class WordDictionary: # 892ms

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        pCrawl = self.root
        length = len(word)
        for level in range(length):
            index = self.charToIndex(word[level])
            if not pCrawl.children[index]:
                pCrawl.children[index] = TrieNode()
            pCrawl = pCrawl.children[index]
        pCrawl.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        pCrawl = self.root
        length = len(word)
        for level in range(length):
            index = self.charToIndex(word[level])
            if index < 0: # dot
                # for every child that isnt None, recursively search
                for child_idx in range(len(pCrawl.children)):
                    if pCrawl.children[child_idx] and self.search( word[:level] + self.indexToChar(child_idx) + word[level+1:] ):
                        return True
                return False
            elif not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]

        return pCrawl != None and pCrawl.end
        
    def charToIndex(self, ch):
        return ord(ch) - ord('a')
    
    def indexToChar(self, idx):
        return chr(idx+ord('a'))

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# another form of Trie, Dynamic filtering!, 76ms, Credits - LeetCode, Best search function for prefix search!
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = collections.defaultdict(set)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        k = len(word)
        self.map[k].add(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        k = len(word)
        
        p = self.map[k]
        if not p:
            return False
        if word in p:
            return True
        
        for i in range(k):
            if word[i] == '.':
                continue
            p = {x for x in p if x[i] == word[i]}
            if not p:
                return False
        return True

        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """