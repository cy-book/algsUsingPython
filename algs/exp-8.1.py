"""
给定整数 A，B 求出将整数A转换为B 需要改变的bit位数
"""


class Solution:
    def bitSwapRequired(self, a: int, b: int) -> int:
        c = a ^ b
        cnt = 0
        for i in range(32):
            if c & (1 << i) != 0:
                cnt += 1
        return cnt


if __name__ == '__main__':
    ns = [[4, 45], [10, 20]]
    solution = Solution()
    for i in ns:
        print(i, " bit swap require ", solution.bitSwapRequired(i[0], i[1]))
