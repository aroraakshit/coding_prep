# https://leetcode.com/problems/sqrtx/

class Solution: # 1988ms
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 0
        while i * i < x:
            i += 1
        return (i if i * i == x else i-1)

class Solution: # 56ms
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1: return x
        # binary search
        left = 0
        right = x
        mid = (left + right) // 2
        while mid*mid != x:
            if mid * mid < x:
                left = mid
            elif mid * mid > x:
                right = mid
            mid = (left + right) // 2
            if abs(right-left) <= 1:
                break
        return mid