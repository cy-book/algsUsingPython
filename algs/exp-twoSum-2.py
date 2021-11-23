"""
hashmap
参考： https://leetcode-cn.com/problems/two-sum/
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [i, hashtable[target - num]]
            hashtable[nums[i]] = i
        return [0, 0]


if __name__ == '__main__':
    numsList = [[2, 7, 11, 15], [3, 2, 4], [3, 3]]
    targetList = [9, 6, 6]
    solution = Solution()
    l = len(numsList)
    for i in range(l):
        print(numsList[i], ", target: ", targetList[i],
              ", result: ", solution.twoSum(numsList[i], targetList[i]))
