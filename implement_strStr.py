class Solution: # 56ms, rabin karp, rolling hash
    def strStr(self, A, B):
        """
        :type haystack A: str
        :type needle B: str
        :rtype: int
        """
        if(len(A) == 0 and len(B) == 0): return 0
        elif len(A) == 0: return -1
        elif (len(B) > len(A)): return -1
        
        p, MOD = 113, 10**9 + 7
        p_inv = pow(p, MOD-2, MOD)
        power = 1

        b_hash = 0
        for x in map(ord, B):
            b_hash += power * x
            b_hash %= MOD
            power = (power * p) % MOD

        a_hash = 0
        power = 1
        for i in range(len(B)):
            a_hash += power * ord(A[i % len(A)])
            a_hash %= MOD
            power = (power * p) % MOD
        
        def check(index):
            return all(A[(i + index) % len(A)] == x for i, x in enumerate(B))
        
        if a_hash == b_hash and check(0): 
            return 0
            
        power = (power * p_inv) % MOD 
        for i in range(len(B), len(A)):
            a_hash = (a_hash - ord(A[(i - len(B)) % len(A)])) * p_inv
            a_hash += power * ord(A[i % len(A)])
            a_hash %= MOD
            if a_hash == b_hash and check(i - len(B) + 1):
                return (i-len(B)+1)
        return -1

class Solution: # 28ms solution, Credits - LeetCode, exhaustive search! 
    def strStr(self, haystack: 'str', needle: 'str') -> 'int':
        dict1={}
        dict2={}
        index=0
        
        if len(needle)==0:
            return 0
        if len(haystack)>0 and needle=="":
            return 0
        
        if needle not in haystack:
            return -1
        else:
            for i in range(len(haystack)-len(needle)+1):
                if len(needle)>0:
                    if haystack[index:index+len(needle)]==needle :
                        return index
                    index+=1
                else:
                    return -1