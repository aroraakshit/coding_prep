class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # merge sorted lists - O(m+n), but desired was O(log(m+n))
        nums3 = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] >= nums2[j]:
                nums3.append(nums2[j])
                j += 1
            else:
                nums3.append(nums1[i])
                i += 1
                
        while i < len(nums1):
            nums3.append(nums1[i])
            i += 1
        
        while j < len(nums2):
            nums3.append(nums2[j])
            j += 1
            
        if len(nums3) % 2:
            return nums3[ len(nums3) // 2 ]
        else:
            return (nums3[len(nums3) // 2] + nums3[len(nums3) // 2 - 1]) / 2