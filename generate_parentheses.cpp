class Solution {
public:
    map<int, vector<string>> memo;
    
    vector<string> generateParenthesis(int n) {
        if (n == 0){
            memo[n] = vector<string>{""};
            return memo[n];
        }
        else if (n == 1){
            memo[n] = vector<string>{"()"};
            return memo[n];
        }
        else if (memo.find(n) != memo.end()){
            return memo[n];
        } else {
            vector<string> lst;
            for(int i=0;i < n; i++){
                auto left = generateParenthesis(i);
                auto right = generateParenthesis(n-1-i);
                for(auto j : left){
                    for (auto k : right){
                        lst.push_back('(' + j + ')' + k);
                    }
                }
            }
            memo[n] = lst;
            return memo[n];
        }
    }
};