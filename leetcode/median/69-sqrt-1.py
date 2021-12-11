'''
给定一个非负整数 x ，计算并返回 x 的平方根，即实现 int sqrt(int x) 函数。

正数的平方根有两个，只输出其中的正数平方根。

如果平方根不是整数，输出只保留整数的部分，小数部分将被舍去。
'''


class Solution:
    def sqrt(self, num: int) -> int:
        left, right = 0, num
        while(left <= right):
            med = left + (right - left) // 2
            sq = med * med
            if(sq == num):
                return med
            elif(sq < num):
                left = med + 1
            else:
                right = med - 1
        return right


if __name__ == '__main__':
    ns = [0, 1, 3, 4, 5, 10]
    solution = Solution()
    for i in ns:
        print(i, " sqrt is: ", solution.sqrt(i))
