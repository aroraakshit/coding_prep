'''
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
'''

class Solution(object): # 100ms
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1_loc = []
        word2_loc = []
        for i in range(len(words)):
            if words[i] == word1:
                word1_loc.append(i)
            elif words[i] == word2:
                word2_loc.append(i)
        if word1_loc == [] or word2_loc == []:
            return -1
        import sys
        m = sys.maxsize
        i = 0
        j = 0
        # print(word1_loc, word2_loc)
        while i < len(word1_loc) and j < len(word2_loc):
            m = min(m, abs(word1_loc[i] - word2_loc[j]))
            if word1_loc[i] > word2_loc[j]:
                j += 1
            elif word2_loc[j] > word1_loc[i]:
                i += 1
            else:
                return m
        return m

class Solution(object): # same
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i1 = -1
        i2 = -1
        m = len(words)
        for i in range(len(words)):
            if words[i] == word1:
                i1 = i
            elif words[i] == word2:
                i2 = i
            if i1 != -1 and i2 != -1:
                m = min(m, abs(i1-i2))
        return m

class Solution(object): # absolutely no idea why this is faster, 24ms
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        size = len(words)
        index1, index2 = size, size
        ans = size

        for i in xrange(size):
            if words[i] == word1:
                index1 = i
                ans = min(ans, abs(index1-index2))
            elif words[i] == word2:
                index2 = i
                ans = min(ans, abs(index1-index2))
        return ans