from collections import defaultdict
class Solution: # 236ms, Credits - LeetCode
    def subarraysWithKDistinct(self, A: 'List[int]', K: 'int') -> 'int':
        dicti, n, i, ans, j = defaultdict(int), len(A), 0, 0, 0
        while i < n:
            
            dicti[A[i]] += 1
            
            while len(dicti) > K:
                dicti[A[j]] -= 1
                if not dicti[A[j]]:
                    del dicti[A[j]]
                j += 1
            if len(dicti) == K:
                k = j
                while k <= i:
                    ans += 1
                    if dicti[A[k]] - 1:
                        dicti[A[k]] -= 1
                        k += 1
                    else:
                        break
                for l in range(j, k):
                    dicti[A[l]] += 1
            i += 1
        return ans

# Credits - LeetCode, based on Sliding window, 608ms
class Window:
    def __init__(self):
        self.count = collections.Counter()
        self.nonzero = 0

    def add(self, x):
        self.count[x] += 1
        if self.count[x] == 1:
            self.nonzero += 1

    def remove(self, x):
        self.count[x] -= 1
        if self.count[x] == 0:
            self.nonzero -= 1

class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        window1 = Window()
        window2 = Window()
        ans = left1 = left2 = 0

        for right, x in enumerate(A):
            window1.add(x)
            window2.add(x)

            while window1.nonzero > K:
                window1.remove(A[left1])
                left1 += 1

            while window2.nonzero >= K:
                window2.remove(A[left2])
                left2 += 1

            ans += left2 - left1

        return ans