# 304 ms, credits: https://blog.csdn.net/fuxuemingzhu/article/details/81807215, python2

import random
import numpy as np
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.probability_distribution = []
        tot = 0
        for i in range(len(w)):
            tot += w[i]
            self.probability_distribution.append(tot)
        self.tot = tot

    def pickIndex(self):
        """
        :rtype: int
        """
        x = random.randint(0, self.tot-1)
        lo = 0
        hi = len(self.probability_distribution) - 1
        while(lo+1 < hi):
            mid = (lo+hi)//2
            if x >= self.probability_distribution[mid]:
                lo = mid
            else:
                hi = mid
        if x < self.probability_distribution[lo]:
            return lo
        return hi

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

# Credits LeetCode, 148ms:
from bisect import *
from random import *
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        tot = 0
        for x in w:
            tot+=x
        self.arr = [0]*len(w)
        self.arr[0] = w[0]*1.0/tot
        for i in xrange(1,len(w)):
            self.arr[i] = self.arr[i-1] + w[i]*1.0/tot
        #print self.arr

    def pickIndex(self):
        """
        :rtype: int
        """
        rand = random()
        return bisect_left(self.arr, rand)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()