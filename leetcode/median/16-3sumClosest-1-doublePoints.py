'''
给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。

返回这三个数的和。

假定每组输入只存在恰好一个解。

思路： 将三数之和转换成两数之和的问题（分离出来第一个数），然后用双指针解决问题
注意于上一题的求解和为零的三个数一题的不同，这里对所有的可能的三元组都要进行计算，以找到最接近的答案（closest）
即，对于sums > target 和 sums < target 的组合，也要计算，它们也有可能成为最终答案
上一题要找的和是一个确定的值，所以当 first, second 确定了了，只能有一个 thrid 与之对应，
因为有确定值，必然就是 sums == target, 所以要判断的情况少一些
'''

# date: 2021-12-11
# author: cy-book

from typing import List


def threeSumClosest(nums: List[int], target: int) -> int:
    n = len(nums)
    if n < 3:
        return 0
    nums.sort()
    ans = target - nums[0] - nums[1] - nums[2]
    for first in range(n):
        if first > 0 and nums[first] == nums[first - 1]:  # 去重 first
            continue
        thrid = n - 1
        tag = target - nums[first]
        for second in range(first + 1, n - 1):
            if second - 1 > first and nums[second] == nums[second - 1]:  # 去重 second
                continue
            while thrid > second:
                # 去重 thrid (对比上一个thrid)
                if thrid + 1 < n and nums[thrid] == nums[thrid + 1]:
                    thrid -= 1
                    continue
                # 三数和 于 target 的接近程度 val =  target - nums[first] - nums[second] - nums[thrid]
                val = tag - nums[thrid] - nums[second]
                if val == 0:    # 如果和等于 target 可以直接返回
                    return target
                ans = ans if abs(ans) < abs(val) else val
                if val > 0:
                    break
                thrid -= 1
            if thrid == second:
                break
    return target - ans


# nums = [-1,2,1,-4], target = 1
# [0,2,1,-3] 1
if __name__ == '__main__':
    inputList = [([-1, 2, 1, -4], 1, 2),
                 ([0, 2, 1, -3], 1, 0), ([3, 4, 5, 5, 7], 13, 13)]
    n = len(inputList)
    for nums, target, ans in inputList:
        outputVal = threeSumClosest(nums, target)
        print(nums, target, outputVal, '(', ans, ')')
