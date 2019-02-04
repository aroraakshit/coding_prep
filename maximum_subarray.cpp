class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        if(nums.size() == 0){
            return 0;
        }
        else if(nums.size() == 1){
            return nums[0];
        }
        
        int max_so_far = nums[0];
        int curr_max = nums[0];
        for(int i=1; i<nums.size(); i++){
            curr_max = max(nums[i], curr_max+nums[i]);
            max_so_far = max(max_so_far, curr_max);
        }
        
        return max_so_far;
    }
};