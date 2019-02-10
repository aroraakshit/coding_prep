class TrieNode:
    def __init__(self):
        self.children = [None for i in range(26)]
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def charToIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self.charToIndex(key[level])
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
        pCrawl.isEndOfWord = True

    def search(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self.charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]

        return pCrawl != None and pCrawl.isEndOfWord

def main():
    keys = ["ABC", "KLA"]
    output = ["Not Present in Trie", "Present in Trie"]
    t = Trie()
    for key in keys:
        t.insert(key.lower())
    print("the: ", output[t.search("the")])

if __name__ == "__main__":
    main()