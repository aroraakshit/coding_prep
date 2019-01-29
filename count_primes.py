class Solution: # 868 ms    
    def buildPrefix(self, MAX): 
        self.prefix =[0]*(MAX + 1)
        # Create a boolean array value in 
        # prime[i] will "prime[0..n]". A  
        # finally be false if i is Not a 
        # prime, else true. 
        prime = [1]*(MAX + 1) 

        p = 2
        while(p * p <= MAX):  

            # If prime[p] is not changed,  
            # then it is a prime 
            if (prime[p] == 1): 

                # Update all multiples of p 
                i = p * 2
                while(i <= MAX): 
                    prime[i] = 0
                    i += p 
            p+=1

        # Build prefix array 
        # prefix[0] = prefix[1] = 0; 
        for p in range(2,MAX+1):  
            self.prefix[p] = self.prefix[p - 1] 
            if (prime[p]==1): 
                self.prefix[p]+=1
    
    def query(self,L, R): 
        return self.prefix[R]-self.prefix[L - 1] 
                
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1: return 0
        else:
            self.buildPrefix(n)
            return self.query(1,n-1)