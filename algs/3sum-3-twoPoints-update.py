'''
利用一些编程技巧让代码更整洁，减少不必要的重写
参考：https://leetcode-cn.com/problems/3sum/solution/san-shu-zhi-he-by-leetcode-solution/
'''


from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    nums.sort
    ans = list()

    for first in range(n):
