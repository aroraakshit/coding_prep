class Solution { // 24ms
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        vector<bool> dp(s.size(),false);
        dp[0] = true;
        for(int i = 1; i<s.size()+1; i++){
            for(int j=0; j<i; j++){
                // cout<<s.substr(j,i-j)<<endl;
                if(dp[j] && find(wordDict.begin(), wordDict.end(), s.substr(j,i-j)) != wordDict.end() ){
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[s.size()];
    }
};