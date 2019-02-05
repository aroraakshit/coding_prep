class Solution:
    def trap(self, height: 'List[int]') -> 'int':
        if(len(height) <= 2):
            return 0
        
        hi = len(height) -1
        lo = 0
        left_max = 0
        right_max = 0
        units = 0
        while(hi>=lo):
            
            if(height[lo] < height[hi]):
                if height[lo] > left_max:
                    left_max = height[lo]
                else:
                    units += left_max - height[lo]
                lo += 1
            else:
                if height[hi] > right_max:
                    right_max = height[hi]
                else:
                    units += right_max - height[hi]
                hi -= 1
                
        return units
                    