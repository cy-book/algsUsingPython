"""
使用划分数组的方法，将两个数组划分成两个数组，其中一个数组的最大值小于另一个数组的最小值
两数组分别从 i, j 处分隔开
i + j = m - i + n - j (偶数)
i + j = m - i + n + 1 (奇数)
==> j = (m + n + 1) // 2 - i
nums1[i - 1] <= nums2[j]
nums2[j - 1] <= nums1[i]
        (推倒)=====> 如果 i 是最大的满足 nums1[i - 1] <= nums2[j] 的数， 有 nums[j - 1] <= nums1[i] 自然成立
median1 = max(nums1[i - 1], nums2[j - 1])
median2 = min(nums1[i], nums2[j])
采用 二分的方式移动索引 i 

参考 : https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-s-114/
"""


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        m, n = len(nums1), len(nums2)
        left, right = 0, m  # right 应等于 m 不能是 m - 1, 处理当 m  = 0 时， 直接导致 left > right
        infinty = 2 ** 40
        median1, median2 = 0, 0
        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i
            # 设置边界， i, j 不会小于 0， 不会大于 m, n, 对于 i == 0, 也有 nums_iml <= nums_j
            nums_iml = (-infinty if i == 0 else nums1[i - 1])
            nums_i = (infinty if i == m else nums1[i])
            nums_jml = (-infinty if j == 0 else nums2[j - 1])
            nums_j = (infinty if j == n else nums2[j])
            if nums_iml <= nums_j:
                # 如果 nums1[i-1] < nums2[j], 则可能找到了满足条件的分界线， 但可能 i 可以继续增大
                median1, median2 = max(
                    nums_iml, nums_jml), min(nums_i, nums_j)
                left = i + 1
            else:
                # 否则一定没有满足条件， 将 i 向左移动， 继续寻找分界线
                right = i - 1
        return (median1 + median2) / 2 if (m + n) & 1 == 0 else median1


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
