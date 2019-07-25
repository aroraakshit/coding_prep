class Solution(object): # Python2 solution, Credits - LeetCode, 20ms, faster than 80% solutions
    #   Topological sort
    def alienOrder(self, words):
        less = []
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    less += a + b,
                    break
        chars = set(''.join(words))
        order = []
        while less:
            free = chars - set(zip(*less)[1])
            if not free:
                return ''
            order += free
            less = filter(free.isdisjoint, less)
            chars -= free
        return ''.join(order + list(chars))