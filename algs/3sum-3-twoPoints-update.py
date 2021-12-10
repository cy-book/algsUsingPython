'''
利用一些编程技巧让代码更整洁，减少不必要的重写
参考：https://leetcode-cn.com/problems/3sum/solution/san-shu-zhi-he-by-leetcode-solution/

通过两重循环嵌套来模拟双指针
'''
# date: 2021-12-10

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    nums.sort()
    ans = list()
    for first in range(n):
        if first > 0 and nums[first] == nums[first - 1]:
            continue
        thrid = n - 1
        target = - nums[first]
        for second in range(first+1, n):
            if second > first + 1 and nums[second] == nums[second - 1]:
                continue
            while second < thrid and nums[second] + nums[thrid] > target:
                thrid -= 1
            if second == thrid:
                break
            if nums[second] + nums[thrid] == target:
                ans.append([nums[first], nums[second], nums[thrid]])
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
