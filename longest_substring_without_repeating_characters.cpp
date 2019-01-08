// https://leetcode.com/problems/longest-substring-without-repeating-characters/
#include <vector>
#include <algorithm>

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if (s.length() == 0) {
            return 0;
        }
        vector<int> v{1};
        int i = 0;
        int j = 1;
        while(j < s.length()){
            // cout<<s.substr(i,j-i)<<" j= "<<j<<"i= "<<i<<endl;
            if ( s.substr(i,j-i).find(s[j]) != std::string::npos ){
                // cout<<"Inside If: "<<s.substr(i,j-i)<<" j= "<<j<<"i= "<<i<<endl;
                v.push_back(s.substr(i,j-i).length());
                // for(auto k:v){
                //     cout<<k<<" ";
                // }
                // cout<<endl;
                while(s[i] != s[j]){
                    i++;
                }
                i++;
                // cout<<"j = "<<j<<endl;
                // cout<<"i = "<<i<<endl;
            }
            // cout<<"\n\n";
            j++;
        }
        v.push_back(s.substr(i,j-i).length());
        return *std::max_element(begin(v),end(v));
    }
};