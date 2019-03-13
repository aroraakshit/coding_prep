class Solution: #176ms, two pointers
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k==0 or len(arr) == 0 or len(arr) < k:
            return 0
        elif len(arr) == k:
            return arr
        diff = [abs(i-x) for i in arr]
        left = 0
        right = len(arr) - 1
        while right-left > k-1:
            if diff[left] > diff[right]:
                left += 1
            else:
                right -= 1
        return arr[left:right+1]

class Solution: # 104ms, Credits - LeetCode, based on binary search!
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:right + k]