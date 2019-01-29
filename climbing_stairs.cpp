class Solution {
public:
    map<int,int> d;
    int climbStairs(int n) {
        if (n == 2){
            return 2;
        }
        else if(n == 1){
            return 1;
        } else if (d.find(n) != d.end()){
            return d[n];
        }
        d[n] = climbStairs(n-2) + climbStairs(n-1);
        return d[n];
    }
};