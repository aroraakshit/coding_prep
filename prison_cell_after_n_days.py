class Solution: # 40ms
    def bit_not(self, n, numbits=8):
        return (1 << numbits) - 1 - n
    
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        if N > 14: # finding pattern: https://leetcode.com/problems/prison-cells-after-n-days/discuss/205684/JavaPython-Find-the-Loop-or-Mod-14 otherwise TLE
            N = N % 14
        
        if N % 14 == 0:
            N = 14
        res = int(''.join([str(i) for i in cells]), 2)
        mask = 2 ** len(cells) - 1
        msk = int('01111110',2)
        # print('{0:08b}'.format(res))
        for i in range(N):
            a = (res << 2) & mask
            # print('a = ', '{0:08b}'.format(a))
            b = res
            # print('b = ','{0:08b}'.format(b))
            res = self.bit_not(b ^ a, numbits = len(cells))
            # print('res after xnor = ','{0:08b}'.format(res))
            res = (res >> 1) & mask
            res = res & msk
            # print('res final = ', '{0:08b}'.format(res))
        return [int(i) for i in '{0:08b}'.format(res)]