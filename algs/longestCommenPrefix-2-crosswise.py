'''
思路： strs的最长公共前缀 等价于 strs[0],strs[1] 的lcp 和 strs[2:] 的最长公共前缀
参考：https://leetcode-cn.com/problems/longest-common-prefix/solution/zui-chang-gong-gong-qian-zhui-by-leetcode-solution/
'''
# date: 2021-12-09


def lcp(s1: str, s2: str) -> str:
    n1, n2 = len(s1), len(s2)
    for i in range(n1):
        if n2 <= i or s2[i] != s1[i]:
            return s1[:i]
    return s1


def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ''
    count = len(strs)
    prefix = strs[0]
    for i in range(1, count):
        if prefix == '':
            return prefix
        prefix = lcp(prefix, strs[i])
    return prefix


if __name__ == '__main__':
    strsList = [['ab', 'a']]
    prefixList = ['a']
    for i in range(len(strsList)):
        prefix = longestCommonPrefix(strsList[i])
        print(strsList[i], prefix, '(', prefixList[i], ')')
