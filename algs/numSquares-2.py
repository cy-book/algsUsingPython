# ！/bin/python3
class Solution:
    def isSquares(self, n: int) -> bool:
        s = int(abs((n**0.5)))
        return s * s == n

    def checkAnwser4(self, n: int) -> bool:
        while n % 4 == 0:
            n = n / 4
        return n % 8 == 7

    def numSquares(self, n: int) -> int:
        if self.isSquares(n):
            return 1
        if self.checkAnwser4(n):
            return 4
        for i in range(1, n):
            if self.isSquares(n - i * i):
                return 2
        return 3


if __name__ == '__main__':
    n = [12, 13]
    solution = Solution()
    for i in n:
        print(solution.numSquares(i))
