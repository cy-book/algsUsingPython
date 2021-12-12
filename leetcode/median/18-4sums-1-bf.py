'''
给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。
请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：

0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。

本题参考 3sums
首先用遍历的方法完成
缺陷： 时间复杂度过高
'''

# date: 2021-12-12
# author: cy-book

from typing import List


def fourSum(nums: List[int], target: int) -> List[List[int]]:
    n = len(nums)
    nums.sort()
    ans = list()
    for first in range(n-3):
        if first > 0 and nums[first] == nums[first - 1]:
            continue
        for second in range(first+1, n-2):
            if second - 1 > first and nums[second] == nums[second - 1]:
                continue
            for thrid in range(second+1, n-1):
                if thrid - 1 > second and nums[thrid] == nums[thrid - 1]:
                    continue
                for fourth in range(thrid+1,  n):
                    if fourth - 1 > thrid and nums[fourth] == nums[fourth - 1]:
                        continue
                    if nums[first] + nums[second] + nums[thrid] + nums[fourth] == target:
                        ans.append([nums[first], nums[second],
                                   nums[thrid], nums[fourth]])
    return ans


if __name__ == '__main__':
    inputList = [([1, 0, -1, 0, -2, 2], 0,
                  [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
                 ([2, 2, 2, 2, 2], 8, [2, 2, 2, 2]),
                 ([-487, -462, -445, -401, -389, -388, -379, -374, -365,
                  -334, -326, -314, -302, -280, -277, -241, -234, -216,
                  -207, -179, -154, -130, -118, -102, -98, -37, -30,
                  -19, 13, 21, 22, 61, 66, 83, 84, 109, 117, 122, 141,
                   162, 170, 205, 209, 223, 232, 240, 246, 250, 264,
                   274, 286, 289, 303, 304, 322, 335, 336, 338, 349,
                   355, 360, 363, 365, 397, 403, 417, 420, 429, 438, 439],
                     1801, [])]
    for nums, target, ans in inputList:
        outputVal = fourSum(nums, target)
        print('intput:', nums, target, ans, sep='  ')
        print('output: ', outputVal)
