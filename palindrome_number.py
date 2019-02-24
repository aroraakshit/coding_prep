class Solution: # 220 ms
    def isPalindrome(self, x: 'int') -> 'bool':
        if x < 0:
            return False
        elif x == int(str(x)[::-1]):
            return True
        else:
            return False

class Solution: # 292ms
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        elif x < 10:
            return True
        else:
            n = len(str(x)) - 1
            while(x%10 == int(x/(10**n)) ):
                x = int(x%(10**n))
                x = int(x//10)
                n -= 2
                if x == 0:
                    return True     
            return False