class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        i1, i2 = 0, 0
        l1, l2 = len(nums1), len(nums2)
        cnt = (l1 + l2) // 2
