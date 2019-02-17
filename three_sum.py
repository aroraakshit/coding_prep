# credits: https://leetcode.com/problems/3sum/discuss/7392/Python-easy-to-understand-solution-(O(n*n)-time).
# O(n*n)
def threeSum(self, nums): # about 1 second
    res = []
    nums.sort()
    for i in xrange(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l +=1 
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1; r -= 1
    return res

# 268ms, credits leetcode!
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #from collections import defaultdict
        from bisect import bisect_left, bisect_right
       
        target = 0
        
        result = []
        length = len(nums)
        
        if length < 3:
            return result
        
        count ={}
        # map the counts
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
            
        keys = list(count.keys())
        keys.sort()
      
        t3 = target // 3
        if t3 in keys and count[t3] >= 3:
            result.append([t3, t3, t3])

        begin = bisect_left(keys, target - keys[-1] * 2)
        end = bisect_left(keys, target * 3)

        for i in range(begin, end):
            a = keys[i]
            if count[a] >= 2 and target - 2 * a in count:
                result.append([a, a, target - 2 * a])

            max_b = (target - a) // 2  # target-a is remaining
            min_b = target - a - keys[-1]  # target-a is remaining and c can max be keys[-1]
            b_begin = max(i + 1, bisect_left(keys, min_b))
            b_end = bisect_right(keys, max_b)

            for j in range(b_begin, b_end):
                b = keys[j]
                c = target - a - b
                if c in count and b <= c:
                    if b < c or count[b] >= 2:
                        result.append([a, b, c])
        return result