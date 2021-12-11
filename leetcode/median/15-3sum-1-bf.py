'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。 

思路：三重遍遍历数组，寻找所有可能的情况
    由于要排除重复的三元组，所以先对数组排序，然后在遍历的时候不重复遍历相同的数字
'''

# date: 2021-12-10
# author: cy-book

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    count = len(nums)
    results = list()
    preX = nums[0] - 1
    for x in range(count-2):
        if nums[x] == preX:
            continue
        preX = nums[x]
        preY = nums[x+1] - 1
        for y in range(x+1, count-1):
            if preY == nums[y]:
                continue
            preY = nums[y]
            preZ = nums[y+1] - 1
            for z in range(y+1, count):
                if preZ == nums[z]:
                    continue
                preZ = nums[z]
                if nums[x] + nums[y] + nums[z] == 0:
                    results.append([nums[x], nums[y], nums[z]])
    return results


if __name__ == '__main__':
    inputList = [[-1, 0, 1, 2, -1, -4], [0, 0, 0], [0, 0, 0, 0],
                 [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]]
    outputList = [[[-1, -1, 2], [-1, 0, 1]], [[0, 0, 0]], [[0, 0, 0]],
                  [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]]
    n = len(inputList)
    for i in range(n):
        ans = threeSum(inputList[i])
        print('input:', inputList[i])
        print('ans:', ans)
        print('output:', outputList[i])
