from collections import defaultdict 
from collections import Counter
#This class represents a undirected graph using adjacency list representation 
class UnionFind: # 2400ms
   
    def __init__(self, lst): 
        self.parent = {i:None for i in lst}
        
    # A utility function to find the subset of an element i 
    def find_parent(self, i):
        if i not in self.parent or self.parent[i] == None: 
            return None
        elif self.parent[i] == i:
            return i
        else:
            return self.find_parent(self.parent[i]) 
  
    # A utility function to do union of two subsets 
    def union(self,x,y): 
        x_set = self.find_parent(x) 
        y_set = self.find_parent(y)
        if x_set == None and y_set == None:
            self.parent[x] = y
            self.parent[y] = y
        elif x_set == None:
            self.parent[x] = y_set
        elif y_set == None:
            self.parent[y] = x_set
        else:
            for i in self.parent.keys():
                if self.parent[i] == x_set:
                    self.parent[i] = y_set
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        union = UnionFind(nums)
        output = len(nums)
        for i in range(len(nums)):
            left = union.find_parent(nums[i]-1)
            right = union.find_parent(nums[i]+1)
            if left == None and right == None:
                union.parent[nums[i]] = nums[i]
            elif left == None:
                union.union(nums[i], right)
            elif right == None:
                union.union(nums[i], left)
            else:
                union.union(nums[i], right)
                union.union(left, right)
            # print(union.parent, left, right)
        
        ctr = Counter()
        for i in union.parent.values():
            ctr[i] += 1
        
        return 0 if list(ctr) == [] else max(list(ctr.values()))

# 32ms, Credits - LeetCode (HashSet and Intelligent Set Building)
def longestConsecutive(self, nums: 'List[int]') -> 'int':
    if not nums:
        return 0
    else:
        result = 1
        s = set(nums)
        for x in s:
            if x-1 not in s:
                cur = x
                while cur in s:
                    cur += 1
                result = max(result, cur-x)
    return result

# another variant, LeetCode
class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak