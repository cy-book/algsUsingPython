'''
思路：根据大字符在前 和 大字符在后两种情况判断当前字符是增量还是减少
参考 https://leetcode-cn.com/problems/roman-to-integer/solution/luo-ma-shu-zi-zhuan-zheng-shu-by-leetcod-w55p/
'''

# date: 2021-12-09

SYMBOL_VALUES = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def romanToInt(s: str) -> int:
    n = len(s)
    ans = 0
    for i, ch in enumerate(s):
        value = SYMBOL_VALUES[ch]
        if i < n-1 and value < SYMBOL_VALUES[s[i+1]]:
            ans -= value
        else:
            ans += value
    return ans


if __name__ == '__main__':
    romanList = ['III', 'IV', 'IX', 'LVIII', 'MCMXCIV']
    valueList = [3, 4, 9, 58, 1994]
    for i in range(len(romanList)):
        ans = romanToInt(romanList[i])
        print(romanList[i], ans, '(', valueList[i], ')')
