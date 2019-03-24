class Solution: #48ms
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        l = nums1 if len(nums1) > len(nums2) else nums2
        s = nums1 if len(nums1) <= len(nums2) else nums2
        overlap = []
        for i in range(len(s)):
            if s[i] in l:
                overlap.append(s[i])
        return overlap

class Solution: # 32ms
    def intersection(self, nums1: 'List[int]', nums2: 'List[int]') -> 'List[int]':
        return list(set(nums1) & set(nums2))