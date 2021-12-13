'''
参考： https://leetcode-cn.com/problems/generate-parentheses/solution/gua-hao-sheng-cheng-by-leetcode-solution/
'''
# date: 2021-12-13
# author: cy-book

from typing import List
from functools import lru_cache


@lru_cache(None)
def generateParenthesis(n: int) -> List[str]:
    ans = list()
    if n == 0:
        return ['']
    for c in range(n):
        for l in generateParenthesis(c):
            for r in generateParenthesis(n-1-c):
                ans.append('({}){}'.format(l, r))
    return ans


if __name__ == '__main__':
    inputList = [8]
    for num in inputList:
        outputVal = generateParenthesis(num)
        print(num, outputVal, sep=': ')
        print(len(outputVal))
