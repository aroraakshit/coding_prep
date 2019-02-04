class Solution { // 4ms, faster than 99.40% of cpp submissions. Based on quicksort / selection idea by leetcode.
public:
    int search(vector<int>& nums, int target) {
        // look for rotation index
        if (nums.size() == 0){
            return -1;
        } 
        else if (nums.size() == 1){
            return (nums[0] == target ? 0 : -1);
        } 
        else if (nums.size() == 2){
            return (nums[0] == target ? 0 : (nums[1] == target ? 1 : -1));
        }
        
        int left = 0;
        int right = nums.size() - 1;
        int mid = (left+right) / 2;
        if(nums[left] < nums[right]){
            // already sorted
            mid = 0;
        }
        else {
            while(left <= right){
                // cout<<left<<" "<<right<<endl;
                mid = (left + right) / 2;
                if (nums[mid] > nums[mid+1]){
                    break;
                }
                else if (nums[mid] >= nums[left]){
                    left = mid+1;
                } 
                else {
                    right = mid-1;
                }
            }
            mid += 1;
        }
        // cout << mid << endl;
        // assuming left == right never happens
        if (target >= nums[mid] and target <= nums[nums.size()-1]){
            left = mid;
            right = nums.size() - 1;
        } else {
            left = 0;
            right = mid-1;
        }
        // cout<<left<<" "<<right<<endl;
        mid = (left + right) / 2;
        while(left <= right){
            // cout<<left<<" "<<right<<endl;
            mid = (left + right) / 2;
            if (nums[mid] == target){
                break;
            }
            if (target < nums[mid]){
                right = mid-1;
            } 
            else {
                left = mid+1;
            }
        }
        
        return (nums[mid] == target ? mid : -1);
        
    }
};