class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        r = 0
        i = 0
        while(n != 0):
            r = r | (n%2 << (32-i-1))
            n = n >> 1
            i += 1
        return r