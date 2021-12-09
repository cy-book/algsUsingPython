'''
给定一个罗马数字，将其转换成整数。
'''

# date: 2021-12-09
# author: cy-book

romanMap = [
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (40, 'XL'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I')
]


def romanToInt(s: str) -> int:
    i = 0
    n = len(s)
    ans = 0
    for value, symbol in romanMap:
        sn = len(symbol)
        while i+sn <= n and s[i:i+sn] == symbol:
            ans += value
            i += sn
    return ans


if __name__ == '__main__':
    romanList = ['III', 'IV', 'IX', 'LVIII', 'MCMXCIV']
    valueList = [3, 4, 9, 58, 1994]
    for i in range(len(romanList)):
        ans = romanToInt(romanList[i])
        print(romanList[i], ans, '(', valueList[i], ')')
