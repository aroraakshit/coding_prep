# Credits - GeeksForGeeks: https://www.geeksforgeeks.org/union-find/ 
from collections import defaultdict 
   
#This class represents a undirected graph using adjacency list representation 
class UnionFind: 
   
    def __init__(self, size): 
        self.parent = [-1 for i in range(size)]
        
    # A utility function to find the subset of an element i 
    def find_parent(self,i): 
        if self.parent[i] == -1: 
            return i 
        else:
            return self.find_parent(parent,parent[i]) 
  
    # A utility function to do union of two subsets 
    def union(self,x,y): 
        x_set = self.find_parent(x) 
        y_set = self.find_parent(y)
        self.parent[x_set] = y_set 