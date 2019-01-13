# Credits: https://www.geeksforgeeks.org/find-a-sorted-subsequence-of-size-3-in-linear-time/
# Python program to fund a sorted subsequence of size 3 
  
class Solution:        
    def increasingTriplet(self, arr):
        if len(arr) < 3: return False
        n = len(arr) 
        max = n-1 # Index of maximum element from right side 
        min = 0 # Index of minimum element from left side 

        # Create an array that will store index of a smaller 
        # element on left side. If there is no smaller element 
        # on left side, then smaller[i] will be -1. 
        smaller = [-1]
        for i in range(1,n): 
            if (arr[i] <= arr[min]): 
                min = i 
                smaller.append(-1)
            else: 
                smaller.append(min)

        # Create another array that will store index of a 
        # greater element on right side. If there is no greater 
        # element on right side, then greater[i] will be -1. 
        greater = [0]*len(arr)
        greater[-1] = -1
        for i in range(n-2,-1,-1): 
            if (arr[i] >= arr[max]): 
                max = i 
                greater[i] = -1
            else: 
                greater[i] = max
        
        # Now find a number which has both a greater number on 
        # right side and smaller number on left side 
        print(smaller)
        print(greater)
        for i in range(0,n): 
            if smaller[i] != -1 and greater[i] != -1: 
                print (arr[smaller[i]], arr[i], arr[greater[i]] )
                return True

        # If we reach here, then there are no such 3 numbers 
        print( "No triplet found")
        return False