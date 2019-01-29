class Solution {
public:
    int countPrimes(int n) {
        if (n <= 1){
            return 0;
        }
        vector<int> prefix(n,0);
        vector<int> prime(n,1);
        int p = 2;
        while(p*p < n){
            if (prime[p] == 1){
                int i = p * 2;
                while(i < n){
                    prime[i] = 0;
                    i += p;
                }
            }
            p += 1;
        }
        
        for (p=2;p<n;p++){
            prefix[p] = prefix[p-1];
            if (prime[p] == 1){
                prefix[p] += 1;
            }
            // cout<<prefix[p]<<' ';
        }
        
        return prefix[n-1];
    }
};