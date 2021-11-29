'''
example: n == 19
    n       odd     lev
    19  0   0       0
    9   9   1       1       pow(x,1)
    4   4   1       2       pow(x,2)
    2   2   0       3       pow(x,4)
    1   1   0       4       pow(x,8)
    0   0   1       5       
假设 n = 2 ** m
temp 一共自乘了 log n 次
    16
    8   8           t 2
    4   4           t 4
    2   2           t 8
    1   1           t 16
'''


class Solution:
    def pow(self, x: float, n: int) -> float:
        if(n < 0):
            x = 1 / x
            n = -n
        ans = 1
        temp = x
        while n != 0:
            if(n % 2 == 1):
                ans *= temp
            temp *= temp
            n //= 2
        return ans


if __name__ == '__main__':
    xns = [[2.1,3], [0,1], [1,0], [2,-2], [3, -3]]
    solution = Solution()
    for xn in xns:
        print("pow ", xn, "is: ", solution.pow(xn[0],xn[1]))