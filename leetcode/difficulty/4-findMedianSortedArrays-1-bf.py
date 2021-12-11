#!/usr/local/bin/python
'''
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 

思路： 暴力求中位数（找到中间小的数）
'''


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        i1, i2 = 0, 0
        l1, l2 = len(nums1), len(nums2)
        cnt = (l1 + l2) // 2 + 1
        left, right = 0, 0
        for i in range(cnt):
            left = right
            if i1 < l1 and i2 < l2:
                if nums1[i1] <= nums2[i2]:
                    right = nums1[i1]
                    i1 += 1
                else:
                    right = nums2[i2]
                    i2 += 1
            elif i1 < l1:
                right = nums1[i1]
                i1 += 1
            elif i2 < l2:
                right = nums2[i2]
                i2 += 1
        if (l1 + l2) & 1 == 1:
            return right
        else:
            return (left + right) / 2


if __name__ == '__main__':
    print('hello macos')
    nums1List = [[1, 3], [1, 2], [0, 0], [], [2]]
    nums2List = [[2], [3, 4], [0, 0], [1], [0]]
    results = [2, 2.5, 0, 1, 1]
    solution = Solution()
    for i in range(len(nums1List)):
        result = solution.findMedianSortedArrays(nums1List[i], nums2List[i])
        print(nums1List[i], ' ', nums2List[i],
              ': ', result, '(', results[i], ')')
