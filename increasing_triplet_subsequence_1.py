# Credits: https://www.geeksforgeeks.org/find-a-sorted-subsequence-of-size-3-in-linear-time/
# Pythion program to fund a sorted subsequence of size 3 
  
def find3numbers(arr): 
    n = len(arr) 
    max = n-1 # Index of maximum element from right side 
    min = 0 # Index of minimum element from left side 
  
    # Create an array that will store index of a smaller 
    # element on left side. If there is no smaller element 
    # on left side, then smaller[i] will be -1. 
    smaller = [0]*10000
    smaller[0] = -1
    for i in range(1,n): 
        if (arr[i] <= arr[min]): 
            min = i 
            smaller[i] = -1
        else: 
            smaller[i] = min
  
    # Create another array that will store index of a 
    # greater element on right side. If there is no greater 
    # element on right side, then greater[i] will be -1. 
    greater = [0]*10000
    greater[n-1] = -1
  
    for i in range(n-2,-1,-1): 
        if (arr[i] >= arr[max]): 
            max = i 
            greater[i] = -1
  
        else: 
            greater[i] = max
  
    # Now find a number which has both a greater number on 
    # right side and smaller number on left side 
    for i in range(0,n): 
        if smaller[i] != -1 and greater[i] != -1: 
            print arr[smaller[i]], arr[i], arr[greater[i]] 
            return
  
    # If we reach here, then there are no such 3 numbers 
    print "No triplet found"
    return
  
  
# Driver function to test above function 
arr = [12, 11, 10, 5, 6, 2, 30] 
find3numbers(arr) 