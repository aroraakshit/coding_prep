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

// Turns out this approach is called closure number
// To enumerate something, generally we would like to express it as a sum of disjoint subsets that are easier to count.

// Consider the closure number of a valid parentheses sequence S: the least index >= 0 so that S[0], S[1], ..., S[2*index+1] is valid. Clearly, every parentheses sequence has a unique closure number. We can try to enumerate them individually.

//Time and Space Complexity : O(\dfrac{4^n}{\sqrt{n}}) // nth catalan number