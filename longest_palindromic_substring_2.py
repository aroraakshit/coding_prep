# longest continuous palindromic sequence - "abcda", will give output "a" or "c", or "d",has to be a continous string
# this solution however times out!
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
            print(temp)
            if temp[::-1] == temp:
                memo[temp] = True
            else:
                for i in range(len(temp)):
                    if temp[:i] not in memo or temp[i+1:] not in memo:
                        queue.append(temp[:i])
                        queue.append(temp[i+1:])
        print(memo)
        return sorted(memo.keys(), key = lambda x: len(x))[-1]