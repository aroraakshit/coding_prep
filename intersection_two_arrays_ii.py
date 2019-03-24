# https://leetcode.com/problems/intersection-of-two-arrays-ii/

from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # # Method 1 - make a dict
        # ans = []
        # cnt = Counter()
        # for i in range(len(nums1)):
        #     cnt[nums1[i]] += 1
        # for i in range(len(nums2)):
        #     if(nums2[i] in dict(cnt)):
        #         ans.append(nums2[i])
        #         cnt[nums2[i]] -= 1
        #         if(cnt[nums2[i]] == 0):
        #             del cnt[nums2[i]]
        # return ans
        
        # Method 2 - what if array was sorted?
        
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        ans = []
        while(i < len(nums1) and j < len(nums2)):
            if(nums1[i] == nums2[j]):
                ans.append(nums1[i])
                j = j + 1
                i = i + 1
            elif(nums1[i] > nums2[j]):
                j = j + 1
            else:
                i = i + 1
        return ans
        
from collections import defaultdict
class Solution: #40ms
    def intersect(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        d1 = defaultdict(int)
        for i in nums1:
            d1[i] += 1
        
        d2 = defaultdict(int)
        for i in nums2:
            d2[i] += 1
        
        final = []
        
        for i in d1.keys():
            if i in d2:
                final += [i]*min(d1[i],d2[i])
        
        return final

# for the code below, 36ms, and credits go to leetcode
import collections
class Solution:
    def intersect(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        counts = collections.defaultdict(int)
        new = []
        
        for num in nums1:
            counts[num] += 1
        
        for num in nums2:
            if counts[num] > 0:
                new.append(num)
                counts[num] -= 1
        
        return new
                