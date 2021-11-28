'''
二分法求中位数( 寻找第 n 大的数)
'''


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        l1, l2 = len(nums1), len(nums2)
        i1, i2 = 0, 0
        cnt = (l1 + l2)//2 + 1
        right, left = 0, 0
        while cnt > 0 and i1 < l1 and i2 < l2:
            left = right
            n = min(cnt//2, l1 - i1, l2 - i2)
            if nums1[i1 + n - 1] <= nums2[i2 + n - 1]:
                right = nums1[i1 + n - 1]
            cnt -= n
        if i1 >= l1:
            right = nums2[i2+n]
            left = nums2[i2 + n-1]
        elif i2 <= l2:
            right = nums1[i1 + n]
            left = nums1[i1 + n - 1]
        if (l1 + l2) & 1 == 1:
            return right
        else:
            return (left+right) / 2


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
