class Solution: #TLE
    def reversePairs(self, nums: List[int]) -> int:
        output = 0
        for j in reversed(range(len(nums))):
            for i in reversed(range(j)):
                if nums[i] > nums[j]*2:
                    output += 1
        return output

from collections import defaultdict
class Solution: # also TLE
    def reversePairs(self, nums: List[int]) -> int:
        output = 0
        d = defaultdict(int)
        for i in range(len(nums)):
            pairs = sum([d[j] for j in d if j>2*nums[i]])
            output += pairs
            d[nums[i]] += 1
        return output

import bisect
class Solution: # based on bisect, 1776ms
    def reversePairs(self, nums: List[int]) -> int:
        output = 0
        ordered = []
        for i in range(len(nums)):
            half_insert = bisect.bisect_right(ordered, nums[i]*2)
            output += len(ordered) - half_insert
            # output += len(ordered[half_insert:])
            # print(output, ordered, half_insert, nums[i])
            bisect.insort_right(ordered,nums[i])
        # print(ordered)
        return output


from collections import defaultdict
import bisect
class Solution: # 1504ms, Fenwick Trees (BIT) based solution, credits - LeetCode
    
    def update(self, BIT, index, val):
        while(index > 0):
            BIT[index] += val
            index -= index & (-index)
            # print(index, "update")
    
    def query(self, BIT, index):
        sum_ = 0
        while(index < len(BIT)):
            sum_ += BIT[index]
            index += index & (-index)
            # print(index, "query", type(index))
        return sum_
    
    def reversePairs(self, nums):
        if len(nums) <= 1:
            return 0
        if len(nums) == 2:
            return int(nums[0] > nums[1]*2)
        output = 0
        n = len(nums)
        nums_copy = sorted([i for i in nums])
        BITS = [0 for i in range(n+1)]
        for i in range(n):
            # print(BITS, nums[i])
            output += self.query(BITS, bisect.bisect_left(nums_copy, nums[i]*2+1) + 1 )
            self.update(BITS, bisect.bisect_left(nums_copy, nums[i]) + 1, 1)
        return output

from collections import defaultdict
import bisect
class Solution(object): # 1420ms, bisect based, Credits - LeetCode
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = []
        res = 0
        for x in nums:
            res += len(seen)-bisect.bisect_right(seen, x*2)
            idx = bisect.bisect_right(seen, x)
            seen[idx:idx] = [x]
        return res

