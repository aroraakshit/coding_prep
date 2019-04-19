from collections import defaultdict
class Solution: # 768ms, BFS based!
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if wordList == [] or not endWord or not beginWord or endWord not in wordList:
            return []
        
        # construct the undirected graph g 
        # where an edge exists between two words that differ only at one character location
        g = defaultdict(list)
        for i in range(len(wordList)):
            for j in range(len(beginWord)):
                g[ wordList[i][:j] + '*' + wordList[i][j+1:] ].append(wordList[i])
        
        queue = [(beginWord, 1, [beginWord])]
        
        visited = defaultdict(list)
        visited[beginWord] = (1, [beginWord])
        
        ans = None
        paths = []
        while queue:
            # print(queue)
            current_word, level, trail = queue.pop(0)
            for i in range(len(beginWord)):
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]
                for word in g[intermediate_word]:
                    if word not in trail:
                        if visited[word] == [] or level + 1 <= min(visited[word])[0]:
                            visited[word].append((level + 1, trail+[word]))
                            queue.append((word, level+1, trail+[word]))
                    
        return [i[1] for i in visited[endWord]]