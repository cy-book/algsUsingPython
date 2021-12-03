'''
按行访问： 根据一个z字所需要的字符个数，可以从字符串中分别提取出来构成结果的每一行的子字符串
第0 行 和第 numRows-1 行： (2*numRows -2) (2* numRows -2) + numRows -1
内部：   2* numRows -2 , 2*numRows -2 + cycLen -i
'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        cycLen = numRows * 2 - 2
        zs = list()
        for i in range(numRows):
            j = 0
            while (j + i) < n:
                zs.append(s[i + j]) # 找到z的顶和底
                if i != 0 and i != (numRows -1) and (j + cycLen - i) < n:
                    #判断这一行是否含有内部(z斜着的部分)
                    zs.append(s[j + cycLen - i])
                j += cycLen
        return ''.join(zs)


if __name__ == '__main__':
    ss = ['PAYPALISHIRING','ab']
    results = ['PAHNAPLSIIGYIR','ab']
    rows = [3,1]
    solution = Solution()
    for i in range(len(ss)):
        print(solution.convert(ss[i], rows[i]),'(',results[i],')')