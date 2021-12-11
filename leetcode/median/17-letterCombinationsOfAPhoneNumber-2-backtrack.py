'''
采用递归的方法遍历

参考：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/submissions/
'''

# date: 2021-12-11

from typing import List

phoneTable = {
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
    def backtrack(index: int):
        if index == len(digits):
            conbinations.append(''.join(conbination))
        else:
            digit = digits[index]
            for ch in phoneTable[digit]:
                conbination.append(ch)
                backtrack(index + 1)
                conbination.pop()

    conbination = list()
    conbinations = list()
    backtrack(0)
    return conbinations


if __name__ == '__main__':
    inputList = [
        ('23', ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])]
    n = len(inputList)
    for digits, ans in inputList:
        outputVal = letterCombinations(digits)
        print(digits, outputVal)
        print(ans)
