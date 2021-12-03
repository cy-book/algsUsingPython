'''
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
'''

from math import ceil

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        numUnitZ = 3 * numRows - 2          # 一个z由多少个字符组成
        counterOfZ = ceil(n / numUnitZ)     # 一共有多少个z 向上取整
        completeZ = n // numUnitZ           # 有多少个完整的 z
        for i in range(n):
            