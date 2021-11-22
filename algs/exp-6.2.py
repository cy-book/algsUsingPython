'''
快速幂 -- 重复平方乘方法
参考 https://blog.csdn.net/weixin_46395886/article/details/113103043
'''


class Solution:
    def fastPower(self, x: int, n: int, b: int) -> int:
        ans = 1
        while n >= 1:
            if(n % 2 == 1):
                ans = ans * x % b
            x *= x
            n //= 2
        return ans


if __name__ == '__main__':
    solution = Solution()
    ns = [[2, 31, 3], [3, 23, 5], [33, 44, 22]]
    for n in ns:
        print(n[0], ' ** ', n[1], ' % ', n[2], ' = ',
              solution.fastPower(n[0], n[1], n[2]), '(', n[0] ** n[1] % n[2], ')')
