# substring version, i.e. "abcda", will give output "ada" or "aca", or "aba", doesn't have to be a continuous string
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        memo = {}
        queue = [s]
        while queue:
            # print(queue)
            temp = queue.pop(0)
            # print(temp)
            if temp[::-1] == temp:
                memo[temp] = True
            else:
                for i in range(len(temp)):
                    if temp[:i]+temp[i+1:] not in memo:
                        queue.append(temp[:i]+temp[i+1:])
        print(memo)
        return sorted(memo.keys(), key = lambda x: len(x))[-1]