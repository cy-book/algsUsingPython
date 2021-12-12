'''
采用双指针的方法，将第三层循环和第四层循环合并，复杂度降到O(3^n)

参考：https://leetcode-cn.com/problems/4sum/solution/si-shu-zhi-he-by-leetcode-solution/
'''

# date: 2021-12-12
# author: cy-book

from typing import List


def fourSum(nums: List[int], target: int) -> List[List[int]]:
    if not nums or len(nums) < 4:
        return []
    n = len(nums)
    nums.sort()
    ans = list()
    val = 0
    for first in range(n-3):
        if first > 0 and nums[first] == nums[first - 1]:
            continue
        # 点睛之笔:两个判断语句将速度加快十倍
        if nums[first] + nums[first + 1] + nums[first + 2] + nums[first + 3] > target:
            break
        if nums[first] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
            continue
        val1 = target - nums[first]
        for second in range(first + 1, n - 2):
            if second - 1 > first and nums[second] == nums[second - 1]:
                continue
            # 作用同上
            if nums[first] + nums[second] + nums[second + 1] + nums[second + 2] > target:
                break
            if nums[first] + nums[second] + nums[n - 2] + nums[n - 1] < target:
                continue
            val2 = val1 - nums[second]
            # 双指针的另一种写法
            l, r = second+1, n-1
            while l < r:
                if val2 - nums[l] - nums[r] == 0:
                    ans.append([nums[first], nums[second],
                               nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1
                elif val2 - nums[l] - nums[r] < 0:
                    r -= 1
                else:
                    l += 1

            '''
            # 由于使用了中间值，所以可以执行更快
            for thrid in range(second + 1, n - 1):
                if thrid - 1 > second and nums[thrid] == nums[thrid - 1]:
                    continue
                val3 = val2 - nums[thrid]
                while fourth > thrid and val3 - nums[fourth] < 0:
                    fourth -= 1
                if fourth == thrid:
                    break
                if val3 == nums[fourth]:
                    ans.append([nums[first], nums[second],
                               nums[thrid], nums[fourth]])
            '''
    return ans


if __name__ == '__main__':
    inputList = [([1, 0, -1, 0, -2, 2], 0,
                  [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
                 ([2, 2, 2, 2, 2], 8, [2, 2, 2, 2]), ]
    for nums, target, ans in inputList:
        outputVal = fourSum(nums, target)
        print('intput:', nums, target, ans, sep='  ')
        print('output: ', outputVal)
