# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution: # 40ms, linear time
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1        
        elif target < nums[0]:
            i = len(nums) - 1
            inc = -1
        elif target > nums[0]:
            i = 0
            inc = 1
        else:
            return 0
        
        while 0 <= i <= len(nums)-1:
            if target == nums[i]:
                return i
            i += inc
        
        return -1


# Wayy easier solution could have been binary search: 36ms O(log(n))

# class Solution:
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         def find_rotate_index(left, right):
#             if nums[left] < nums[right]:
#                 return 0
            
#             while left <= right:
#                 pivot = (left + right) // 2
#                 if nums[pivot] > nums[pivot + 1]:
#                     return pivot + 1
#                 else:
#                     if nums[pivot] < nums[left]:
#                         right = pivot - 1
#                     else:
#                         left = pivot + 1
                
#         def search(left, right):
#             """
#             Binary search
#             """
#             while left <= right:
#                 pivot = (left + right) // 2
#                 if nums[pivot] == target:
#                     return pivot
#                 else:
#                     if target < nums[pivot]:
#                         right = pivot - 1
#                     else:
#                         left = pivot + 1
#             return -1
        
#         n = len(nums)
        
#         if n == 0:
#             return -1
#         if n == 1:
#             return 0 if nums[0] == target else -1 
        
#         rotate_index = find_rotate_index(0, n - 1)
        
#         # if target is the smallest element
#         if nums[rotate_index] == target:
#             return rotate_index
#         # if array is not rotated, search in the entire array
#         if rotate_index == 0:
#             return search(0, n - 1)
#         if target < nums[0]:
#             # search on the right side
#             return search(rotate_index, n - 1)
#         # search on the left side
#         return search(0, rotate_index)
