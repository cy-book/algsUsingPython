'''
思路： 
    （1）每次从 x 中取出最后一位，接入 rev的最后一位
        digit = x % 10  , x = (x - digit) // 10
        注意： 如果 x 是负数， x % 10 也是正数， 需要加上一个模
    （2）判断溢出
        rev < INT_MIN or rev > INT_MAX 
        但条件是在32位的机器上， 所以 rev 本身不会超过 32 位的限制
        在 rev 接入新的一位时进行溢出判断

参考： https://leetcode-cn.com/problems/reverse-integer/solution/zheng-shu-fan-zhuan-by-leetcode-solution-bccn/
'''


def reverse(x: int) -> int:
    INT_MAX, INT_MIN = 2 ** 31 - 1, -2 ** 31  # 设定溢出界限
    rev = 0  # 翻转后的数
    while x != 0:
        if rev < INT_MIN // 10 + 1 or rev > INT_MAX // 10:      # 溢出判断
            return 0
        digit = x % 10
        if x < 0 and digit > 0:
            digit -= 10
        x = (x - digit) // 10
        rev = rev * 10 + digit
    return rev


if __name__ == '__main__':
    integerList = [123, -123, -120, 0]
    resultsList = [321, -321, -21, 0]
    for i in range(len(integerList)):
        results = resultsList[i]
        val = integerList[i]
        ans = reverse(val)
        print(val, ": ", ans, '(', results, ')')
