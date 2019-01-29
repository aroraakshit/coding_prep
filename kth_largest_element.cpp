using namespace std; // 8ms
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
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