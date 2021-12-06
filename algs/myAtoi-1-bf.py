'''
请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。

函数 myAtoi(string s) 的算法如下：

读入字符串并丢弃无用的前导空格
检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
如果整数数超过 32 位有符号整数范围 [−231,  231 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被固定为 −231 ，大于 231 − 1 的整数应该被固定为 231 − 1 。
返回整数作为最终结果。
注意：

本题中的空白字符只包括空格字符 ' ' 。
除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符。
'''

# date: 2021-12-06
# author: cy-book


def myAtoi(s: str) -> int:
    MAX_INT, MIN_INT = 2**31 - 1,  2**31
    n, i = len(s), 0
    while i < n and s[i].isspace():
        i += 1
    if i >= n:
        return 0
    if s[i] != '-':
        if s[i] == '+':
            d = 0
            i += 1
        elif s[i].isdigit():
            d = 0
        else:
            return 0
    else:
        d = 1
    s = s[i+d:]
    ans = 0
    for i in range(len(s)):
        if s[i].isdigit():
            ans = ans * 10 + int(s[i])
            ans = min(MAX_INT, ans) if d == 0 else min(MIN_INT, ans)
        else:
            break
    return ans if d == 0 else -ans


if __name__ == '__main__':
    examples = ['123', '234', '+456', '-134',
                '   356adb', '  -423dd3', ' -42', '']
    results = [123, 234, 456, -134, 356, -423, -42, 0]
    for i in range(len(examples)):
        ans = myAtoi(examples[i])
        print(examples[i], ans, '(', results[i], ')')
