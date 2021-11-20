'''
实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。
'''


class Solution:
    def pow(self, x: float, n: int) -> float:
        if (n < 0):
            n = -n
            x = 1 / x
        temp = 1
        while n > 1:
            if n & 1 == 1: # is odd
                temp *= x
            x*=x
            n //=2
        return temp * x


if __name__ == '__main__':
    xns = [[2.1,3], [0,1], [1,0], [2,-2], [3, -3]]
    solution = Solution()
    for xn in xns:
        print("pow ", xn, "is: ", solution.pow(xn[0],xn[1]))