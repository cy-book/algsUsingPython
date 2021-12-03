'''
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

思路： 按行排序 
根据字符串索引很容易找到它在z字符的行数,只需要两个参数，当前行与下一行的方向
'''

from math import ceil

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        rows = [[] for _ in range(min(n, numRows))]
        d = -1      #设置方向
        curIndex = 0    #设置当前行
        for i in range(n):
            rows[curIndex].append(s[i])
            # 每次走到z的最上方或者最下方时候，就要改变当前行的方向
            if curIndex == (min(n,numRows) -1) or curIndex == 0:
                d = -d
            curIndex += d
        zs = ""
        for i in rows:
            zs = zs +  "".join(rows[i])
        return zs
    

if __name__ == '__main__':
    ss = ['PAYPALISHIRING','ab']
    results = ['PAHNAPLSIIGYIR','ab']
    rows = [3,1]
    solution = Solution()
    for i in range(len(ss)):
        print(solution.convert(ss[i], rows[i]),'(',results[i],')')
