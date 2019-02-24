class Solution(object): #56ms, Credits: LeetCode Discussion
    def __init__(self):
        self.memo = {}
    def isMatch(self, text, pattern):
        if not pattern:
            return not text
        if (text, pattern) in self.memo:
            return self.memo[(text, pattern)]
        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            self.memo[(text, pattern)] = (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            self.memo[(text, pattern)] = first_match and self.isMatch(text[1:], pattern[1:])
        return self.memo[(text, pattern)]