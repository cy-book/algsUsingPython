'''
f(x) = x*x + num
f`(x) = 2*x = k
y0 = x0 * x0 - num
l: y - y0 = k(x - x0)
    =>  y = 0 :  x = -y0/k + x0   =    -(x0 * x0 - num)/(2 * x0)+ x0 = (x0 + num/x0) /2
        x = (x0 + num/x0) /2
'''


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x0 = num+1
        x1 = num+2
        while x1 - x0 > 1e-6:
            x1 = x0
            x0 = (x1 + num/x1)/2
        return int(x0) * int(x0) == num


if __name__ == '__main__':
    nums = [1, 4, 9, 10, 16, 18, 36, 37]
    solution = Solution()
    for i in nums:
        print(i, 'is perfect square:', solution.isPerfectSquare(i))
