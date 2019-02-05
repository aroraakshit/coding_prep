class Solution {
public:
    int trap(vector<int>& height) {
        
        if(height.size() <= 2){
            return 0;
        }
        
        int left_max = 0;
        int right_max = 0;
        int hi = height.size()-1;
        int lo = 0;
        int units = 0;
        while(lo <= hi){
            
            if(height[lo] < height[hi]){
                if(height[lo] > left_max){
                    left_max = height[lo];
                }
                else {
                    units += left_max - height[lo];
                }
                lo += 1;
            }
            else {
                if(height[hi] > right_max){
                    right_max = height[hi];
                }
                else {
                    units += right_max - height[hi];
                }
                hi -= 1;
            }
                
        }
        return units;
    }
};