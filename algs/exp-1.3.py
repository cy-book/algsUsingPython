class Solution:
    def numSquares(self, n: int) -> int:
        while n % 4 == 0:
            n //= 4
        if n % 8 == 7:
            return 4
        for i in range(n + 1):
            temp = i * i
            if temp <= n:
                if int((n - temp)**0.5)**2 + temp == n:
                    return 1 + (0 if temp == 0 else 1)
            else:
                break
        return 3


if __name__ == '__main__':
    n = [12, 13]
    solution = Solution()
    for i in n:
        print(solution.numSquares(i))
