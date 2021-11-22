'''
快速幂 -- 重复平方乘方法
参考 https://blog.csdn.net/weixin_46395886/article/details/113103043
'''


class Solution:
    def fastPower(self, x: int, n: int, b: int) -> int:
        ans = x
        while n >= 1:
            if(n % 2 == 1):
                x *= x
            ans = ans * x % b
            n //= 2
        return ans