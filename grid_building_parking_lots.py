# A company wants to develop an office park in a grid where each cell represents a potential building lot. The goal is for the furthest of all lots to be as near as possible to an office building. Determine the building placement to minimize the distance of most distant lot is from an office building. Distance is measured in horizontal and vertical directions, i.e. diagonal distance measurement is not considered.

# For example, there are n = 3 office buildings to build on a grid that is w - 4 lots wide and h = 4 lots high. An optimal grid placement sets any lot within two units distance of an office building. In the distance grid below, offices are cells at distance 0. The other cells represent the distances from the nearest office.
# 1 0 1 2
# 2 1 2 1
# 1 0 1 0
# 2 1 2 1

# Function Description:
# Complete the function findMinDistance in the editor below. The function must return an integer that denotes the maximal value among shortest distances to the closest office for each cell.
# findMinDistance has the following parameters: w (an integer, the width of the grid), h (an integer, the height of the grid), n (an integer, the number of buildings to be placed)
# Constraints: 1 <= w,h; w*h <= 28; 1 <= n <= 5; n <= w*h;

def calculateDistances(matrix):
    

def findMinDistance(w,h,n):
    if n == 1:
        return max(w,h) // 2
    else:
        mat = [[w*h for j in range(w)] for i in range(h)]
        mat[0][0] = 0
        mat = calculateDistances(mat)
        for i in range(n-1):


print(findMinDistance(2,3,2)) #should give 1
# because:
# 0 1
# 1 1
# 1 0

print(findMinDistance(5,1,1)) #should give 2
# because:
# 2 1 0 1 2