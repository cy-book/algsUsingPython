class Solution:
    def sqrt(self, num: int) -> float:
        x0, x1 = num+1, num+2
        while x1 - x0 > 1e-6:
            x1 = x0
            x0 = (x1 + num/x1) / 2
        return x0


if __name__ == '__main__':
    ns = [0, 1, 3, 4, 5, 10]
    solution = Solution()
    for i in ns:
        print(i, " sqrt is: ", solution.sqrt(i))
