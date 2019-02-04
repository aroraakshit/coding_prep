#include<map>

using namespace std;

class Solution { // O(n) time and space
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> d;
        for (int i=0; i< nums.size(); i++){
            if (d.find(nums[i]) != d.end()){
                return vector<int>{d[nums[i]], i};
            } else {
                d[target - nums[i]] = i;
                // cout<<nums[i]<<endl;
                // for(auto elem : d)
                // {
                //    std::cout << elem.first << " " << elem.second << "\n";
                // }
                // cout<<"done!\n\n"<<endl;
            }
        }
        return vector<int>{};
    }
};