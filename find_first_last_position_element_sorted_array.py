import bisect
class Solution: # 40ms
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or target == None or target not in nums:
            return [-1,-1]
        
        return [bisect.bisect_left(nums, target), bisect.bisect_right(nums, target)-1]


class Solution: # 32ms, Credits - leetcode, based on Binary Search
    def searchRange(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        def findleft(nums, i, j, target):
            if i == j:
                if nums[i] == target: return i
                else: return -1
            else:            
                mid = int((i+j)/2)
                if nums[mid] >= target:
                    return findleft(nums, i, mid, target)
                else:
                    return findleft(nums, mid+1, j, target)
                
        def findright(nums, i, j, target):
            if i == j: return i
            else:            
                mid = int((i+j)/2)
                if nums[mid] > target:
                    return findright(nums, i, mid, target)
                else:
                    return findright(nums, mid+1, j, target)
        
        if nums == None or len(nums) == 0: return [-1, -1]
        else: 
            left = findleft(nums, 0, len(nums)-1, target)
            right = findright(nums, 0, len(nums)-1, target)
            if nums[right] == target:
                return [left, right]
            elif right != 0 and nums[right-1] == target:
                return [left, right-1]
            else:
                return [-1, -1]