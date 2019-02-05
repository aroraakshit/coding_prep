class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> products{1};
        for(int i =1; i<nums.size();i++){
            products.push_back(products[i-1]*nums[i-1]);
        }
        
        int p = 1;
        for(int i = nums.size()-1; i>=0 ;i--){
            products[i] = products[i] * p;
            p = p * nums[i];
        }
        
        
        
        return products;
    }
};