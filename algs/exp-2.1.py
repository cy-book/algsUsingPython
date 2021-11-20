# 给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
# 进阶：不要 使用任何内置的库函数，如  sqrt 。


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1, num + 1):
            temp = i * i
            if temp > num:
                return False
            if temp == num:
                return True
        return False


if __name__ == '__main__':
    nums = [1, 12, 8, 0, 16, 18, 36]
    solution = Solution()
    for i in nums:
        print(i, 'is perfect square:', solution.isPerfectSquare(i))
