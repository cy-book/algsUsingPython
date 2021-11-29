'''
二分法求中位数( 寻找第 n 大的数)
'''


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        def getKthElement(k):
            l1, l2 = len(nums1), len(nums2)
            i1, i2 = 0, 0
            while True:
                # 考虑边界情况
                if i1 >= l1:
                    return nums2[i2 + k - 1]
                if i2 >= l2:
                    return nums1[i1 + k - 1]
                if k == 1:
                    return min(nums1[i1], nums2[i2])
                # 折半删减
                half = k // 2
                # newIndex 位置是要排除的一组元素的结束位置索引
                newIndex1 = min(l1, i1 + half) - 1
                newIndex2 = min(l2, i2 + half) - 1
                if nums1[newIndex1] <= nums2[newIndex2]:
                    # 排除的子数组为[i...newIndex], 共 newIndex - i + 1 个数
                    k -= (newIndex1 - i1 + 1)
                    i1 = newIndex1 + 1
                else:
                    k -= (newIndex2 - i2 + 1)
                    i2 = newIndex2 + 1
        m, n = len(nums1), len(nums2)
        totalLength = m + n
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2


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
