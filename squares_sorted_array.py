class Solution: # 164ms
    def sortedSquares(self, A: List[int]) -> List[int]:
        A = [abs(i)*abs(i) for i in A]
        return sorted(A)

class Solution: # 264ms
    def sortedSquares(self, A: List[int]) -> List[int]:
        left = 0
        right = len(A) - 1
        
        while(left < right):
            if abs(A[left]) < abs(A[right]):
                A[right] *= A[right]
                right -= 1
            else:
                A.insert(right+1, A[left]**2)
                left += 1
                
        A[left] *= A[left]
            
        return A[left:]