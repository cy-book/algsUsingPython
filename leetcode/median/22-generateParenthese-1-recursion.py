'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
'''

from typing import List


def appendParentheis(s: str, l: int, r: int) -> List[str]:
    ans = list()
    if r == 0:
        return []
    if l == 0:
        return [s+')'*r]
    if l > 0:
        ans += appendParentheis(s+'(', l-1, r)
    if r - l > 0:
        ans += appendParentheis(s+')', l, r-1)
    return ans


def generateParenthesis(n: int) -> List[str]:
    return appendParentheis('', n, n)


if __name__ == '__main__':
    inputList = [8]
    for num in inputList:
        outputVal = generateParenthesis(num)
        print(num, outputVal, sep=': ')
        print(len(outputVal))
