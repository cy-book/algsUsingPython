'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

采用循环的方式遍历
'''

# date: 2021-12-11
# author: cy-book

from typing import List

phoneTable = {
    '1': [''],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}


def letterCombinations(digits: str) -> List[str]:
    if not digits:
        return []
    n = 4 - len(digits)
    digits = n * '1' + digits
    ans = list()
    for first in phoneTable[digits[0]]:
        val1 = first
        for second in phoneTable[digits[1]]:
            val2 = val1 + second
            for thrid in phoneTable[digits[2]]:
                val3 = val2 + thrid
                for fourth in phoneTable[digits[3]]:
                    ans.append(val3 + fourth)
    return ans


if __name__ == '__main__':
    inputList = [
        ('23', ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])]
    n = len(inputList)
    for digits, ans in inputList:
        outputVal = letterCombinations(digits)
        print(digits, outputVal)
        print(ans)
