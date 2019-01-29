import heapq
class Solution: # 44ms
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # idea is to populate a min heap of capacity k
        heap = []
        
        for i in range(len(nums)):
            if len(heap) == k and heap[0] < nums[i]:
                heapq.heappop(heap)
                heapq.heappush(heap,nums[i])
            elif len(heap) != k:
                heapq.heappush(heap,nums[i])
        return heapq.heappop(heap)