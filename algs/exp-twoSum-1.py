'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？
violent algorithm
'''


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        l = len(nums)
        for i in range(l):
            for j in range(i+1, l):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == '__main__':
    numsList = [[2, 7, 11, 15], [3, 2, 4], [3, 3]]
    targetList = [9, 6, 6]
    solution = Solution()
    l = len(numsList)
    for i in range(l):
        print(numsList[i], ", target: ", targetList[i],
              ", result: ", solution.twoSum(numsList[i], targetList[i]))
