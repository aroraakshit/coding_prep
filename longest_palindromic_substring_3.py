# longest continuous palindromic sequence - "abcda", will give output "a" or "c", or "d",has to be a continous string
# this solution however times out! or runs out of memory
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        memo = {} 
        queue = [s]
        max_l = 0
        tot = 0
        while queue:
            tot += 1
            temp = queue.pop(0)
            # print(temp)
            if (len(temp) < 3 or len(set(temp)) != len(temp)) and temp[::-1] == temp:
                memo[temp] = True
                if len(temp) > max_l:
                    max_l = len(temp)
            else:
                memo[temp] = False
                for i in range(len(temp)):
                    if temp[:i] not in memo and len(temp[:i]) > max_l:
                        queue.append(temp[:i])
                    if temp[i+1:] not in memo and len(temp[i+1:]) > max_l:
                        queue.append(temp[i+1:])
        # print(memo)
        print(tot)
        return sorted(memo.keys(), key = lambda x: len(x) if memo[x]==True else 0)[-1]
        