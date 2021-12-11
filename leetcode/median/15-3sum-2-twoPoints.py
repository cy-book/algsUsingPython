'''
思路： a + b + c == 0  ==> b + c == -a
将三数之和转换成两数之和，再使用双指针遍历数组
'''


# date: 2021-12-10
# author: cy-book

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    if len(nums) < 3:
        return []
    nums = sorted(nums)
    n = len(nums)
    preValue = nums[0] - 1
    ans = list()
    for i in range(n-2):
        if nums[i] == preValue:
            continue
        preValue = nums[i]
        val = - nums[i]
        l, r = i + 1, n - 1
        while l < r:
            if nums[l] + nums[r] == val:
                ans.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while r > l and nums[r] == nums[r - 1]:
                    r -= 1
                r -= 1
                l += 1
            elif nums[l] + nums[r] < val:
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                l += 1
            else:
                while r > l and nums[r] == nums[r - 1]:
                    r -= 1
                r -= 1
    return ans


if __name__ == '__main__':
    inputList = [[-2, 0, 1, 1, 2], [-1, 0, 1, 2, -1, -4], [0, 0, 0], [0, 0, 0, 0],
                 [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]]
    outputList = [[[-2, 0, 2], [-2, 1, 1]], [[-1, -1, 2], [-1, 0, 1]], [[0, 0, 0]], [[0, 0, 0]],
                  [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]]
    n = len(inputList)
    for i in range(n):
        ans = threeSum(inputList[i])
        print('input:', inputList[i])
        print('ans:', ans)
        print('output:', outputList[i])
