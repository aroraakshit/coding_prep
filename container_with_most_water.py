class Solution: # TLE
    def maxArea(self, height: List[int]) -> int:
        if len(height) <= 1:
            return -1
        elif len(height) == 2:
            return min(height)
        
        maxArea = 0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                maxArea = max(maxArea, min(height[i], height[j]) * (j-i) )
                
        return maxArea

# two pointer approach     
class Solution: # 72ms
    def maxArea(self, height: List[int]) -> int:
        if len(height) <= 1:
            return -1
        elif len(height) == 2:
            return min(height)
        
        left = 0
        right = len(height) - 1
        maxArea = 0
        
        while(left < right):
            maxArea = max( maxArea, min(height[left], height[right]) * (right-left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
                
        return maxArea