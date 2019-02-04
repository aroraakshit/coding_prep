using namespace std; // 8ms
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) { // O(N*log(k)) (adding one element in heap is log(k)) time complexity, O(k) to store heap elements
        priority_queue <int, vector<int>, greater<int>> pq;
        for (auto i: nums){
            if (pq.size() == k && pq.top() < i){
                pq.pop();
                pq.push(i);
            } else if (pq.size() != k){
                pq.push(i);
            }
        }
        return pq.top();
    }
};

// Another approach could have been QuickSelect (Hoar's selection algorithm) with time complexity O(N) average case and O(N^2) worse case.
// space complexity O(N)
// class Solution: # Credits: Leet Code
//     def findKthLargest(self, nums, k):
//         """
//         :type nums: List[int]
//         :type k: int
//         :rtype: int
//         """
//         def partition(left, right, pivot_index):
//             pivot = nums[pivot_index]
//             # 1. move pivot to end
//             nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  
            
//             # 2. move all smaller elements to the left
//             store_index = left
//             for i in range(left, right):
//                 if nums[i] < pivot:
//                     nums[store_index], nums[i] = nums[i], nums[store_index]
//                     store_index += 1

//             # 3. move pivot to its final place
//             nums[right], nums[store_index] = nums[store_index], nums[right]  
            
//             return store_index
        
//         def select(left, right, k_smallest):
//             """
//             Returns the k-th smallest element of list within left..right
//             """
//             if left == right:       # If the list contains only one element,
//                 return nums[left]   # return that element
            
//             # select a random pivot_index between 
//             pivot_index = random.randint(left, right)     
                            
//             # find the pivot position in a sorted list   
//             pivot_index = partition(left, right, pivot_index)
            
//             # the pivot is in its final sorted position
//             if k_smallest == pivot_index:
//                  return nums[k_smallest]
//             # go left
//             elif k_smallest < pivot_index:
//                 return select(left, pivot_index - 1, k_smallest)
//             # go right
//             else:
//                 return select(pivot_index + 1, right, k_smallest)

//         # kth largest is (n - k)th smallest 
//         return select(0, len(nums) - 1, len(nums) - k)
