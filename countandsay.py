# 36ms, faster than 94.6%
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        translation = self.countAndSay(n-1)
        answer = ""
        freq = 0
        it = 0
        while it < len(translation):
            if it > 0 and translation[it] != translation[it-1]:
                answer += str(freq) + translation[it-1]
                freq = 0
            freq += 1
            it += 1
        answer += str(freq) + translation[it-1]
        return answer

# an iterative solution is faster: 24ms, Credits - LeetCode:
class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for _ in range(n - 1):
            number, previous = 1, res[0]
            tmp = ""
            for c in res[1:]:
                if c == previous:
                    number += 1
                else:
                    tmp += str(number) + previous
                    number = 1
                    previous = c
            tmp += str(number) + previous
            res = tmp
        return res