'''
给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。

如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方。
'''


class Solution:
    def isPowerOfTwo(self, num: int) -> bool:
        if(num <= 0):
            return False
        x0 = num
        while x0 != 1:
            x1 = x0//2
            if(x1 * 2 != x0):
                return False
            x0 = x1
        return True


if __name__ == '__main__':
    ns = [0, 1, 4, 5, 16, 17]
    solution = Solution()
    for i in ns:
        print(i, 'is power of 2: ', solution.isPowerOfTwo(i))
