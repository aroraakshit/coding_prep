class Solution: # 40ms, faster than 99.3%
    def largestNumber(self, nums: List[int]) -> str:
        if nums != []:
            n = list(reversed(sorted([str(i) for i in nums])))
            i = len(n) - 2
            # print(n)
            while i >= 0:
                while i < len(n) - 1 and n[i+1][0] == n[i][0] and int(n[i+1] + n[i]) > int(n[i] + n[i+1]):
                    n[i+1], n[i] = n[i], n[i+1]
                    i += 1
                i -= 1
            return str(int(''.join(n)))
        return ""


class LargerNumKey(str): # Credits - LeetCode, 40ms, Interesting use of map function for custom comparator op
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num