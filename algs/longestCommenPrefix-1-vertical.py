'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

'''
# date: 2021-12-09
# author: cy-book


def longestCommonPrefix(strs: list[str]) -> str:
    n = len(strs)
    if n == 0:
        return ''
    exampleStr = strs[0]
    exampleStrLen = len(exampleStr)
    prefix = list()
    for i in range(exampleStrLen):
        nextCh = exampleStr[i]
        for j in range(1, n):
            if len(strs[j]) <= i or strs[j][i] != nextCh:
                return ''.join(prefix)
        prefix.append(nextCh)
    return ''.join(prefix)


def longestCommonPrefix2(strs: list[str]) -> str:
    if not strs:
        return ''
    length, count = len(strs[0]), len(strs)
    for i in range(length):
        ch = strs[0][i]
        if any(len(strs[j]) == i or strs[j][i] != ch for j in range(count)):
            return strs[0][:i]
    return strs[0]


if __name__ == '__main__':
    strsList = [['ab', 'a']]
    prefixList = ['a']
    for i in range(len(strsList)):
        prefix = longestCommonPrefix2(strsList[i])
        print(strsList[i], prefix, '(', prefixList[i], ')')
