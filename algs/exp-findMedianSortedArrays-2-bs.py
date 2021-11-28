'''
二分法求中位数( 寻找第 n 大的数)
'''


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        l1, l2 = len(nums1), len(nums2)
        i1, i2 = 0, 0       # i1, i2 指向的应是nums1 和nums2 的第一个有效位置
        cnt = (l1 + l2)//2  # cnt 是要找到的第两数组合并后的第cnt个位置的数
        right, left = 0, 0
        while cnt > 0 and i1 < l1 and i2 < l2:
            left = right
            n = min((cnt)//2, l1 - i1 - 1, l2 - i2 - 1)  # 这一轮要排除前n个最小的数
            if nums1[i1 + n] <= nums2[i2 + n]:
                right = nums1[i1 + n]
                i1 += n + 1
            else:
                right = nums2[i2 + n]
                i2 += n + 1
            cnt -= n        # 排除了n个数
        # 还需要排除cnt个数
        if i2 < l2:
            right = nums2[i2+cnt]
            left = nums2[i2 + cnt-1]
        elif i1 < l1:
            right = nums1[i1 + cnt]
            left = nums1[i1 + cnt - 1]
        print('left: ', left, ' right: ', right)
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
