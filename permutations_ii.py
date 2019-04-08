class Solution: # 448ms
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 1:
            return [ [nums[0]] ]
        
        ans = []
        for i in range(len(nums)):
            copy = nums.copy()
            temp = [nums[i]]
            copy.pop(i)
            res = self.permuteUnique(copy)
            for j in (res):
                if temp + j not in ans:
                    ans.append( temp + j )
        return ans

class Solution: # 56ms, same idea, Credits - LeetCode
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        num=nums
        if not num:
            return []
        num.sort()
        ret = [[]]
        for n in num:
            new_ret = []
            l = len(ret[-1])
            for seq in ret:
                for i in range(l, -1, -1):
                    if i < l and seq[i] == n:
                        break
                    new_ret.append(seq[:i] + [n] + seq[i:])
            ret = new_ret
        return ret

class Solution: # 68ms, Credits - LeetCode, smallest solution using list comprehension
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res =[[]]
        for c in nums:
            res = [rest[:j]+[c]+rest[j:] for rest in res for j in range((rest+[c]).index(c)+1)]
        return res

class Solution: # dfs based solution, 60ms, Credits - LeetCode
    def permuteUnique(self, nums: 'List[int]') -> 'List[List[int]]':
        if not nums or len(nums) == 0:
            return []
        nums.sort()
        res = []
        self.dfs(nums, [], [False for _ in range(len(nums))], res)
        return res
    
    def dfs(self, nums, lst, used, res):
        if len(lst) == len(nums):
            res.append(list(lst))
            return
        prev = -1
        for i in range(len(nums)):
            if used[i]:
                continue
            if prev >= 0 and nums[i] == nums[prev]:
                continue
            lst.append(nums[i])
            used[i] = True
            self.dfs(nums, lst, used, res)
            used[i] = False
            lst.pop()
            prev = i