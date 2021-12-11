'''
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

bf alg
'''

# date: 2021-12-07
# author: cy-book


def isMatch(s: str, p: str) -> bool:
    i1, i2 = 0, 0
    n1, n2 = len(s), len(p)
    while i1 < n1 and i2 < n2:
        c = s[i1]
        m = p[i2]
        if i2 + 1 < n2 and p[i2+1] == '*':
            i2 += 2
            while i1 < n1:
                # if i2 < n2:
                #m2 = p[i2]
                # 关于*字符到底要匹配多少字符的问题
                # 当前的匹配可能会占用后面字符的位置
                # if s[i1] == m2 or m2 == '.':
                # 解决的方法用了最费时的不停尝试，可改进为动态规划，利用已有匹配去匹配更长序列
                if isMatch(s[i1:], p[i2:]):
                    return True
                if s[i1] == m or m == '.':
                    i1 += 1
                    continue
                else:
                    break

        elif c == m or m == '.':
            i1 += 1
            i2 += 1
            continue
        else:
            return False
    if i1 < n1:
        return False
    elif i2 >= n2:
        return True
    else:  # 当剩下的 pattern 串可以匹配空字符串是，依然匹配成功
        while i2 < n2:
            if i2 + 1 < n2 and p[i2 + 1] == '*':
                i2 += 2
            else:
                return False
        return True


s = 'a'
p = 'ab*'
isMatch(s, p)


if __name__ == '__main__':
    exampleStr = ['aa', 'aa', 'ab', 'aab',
                  'mississippi', 'mississippi', 'ab', 'aaa', 'mississippi', 'aaa', 'a'
                  ]
    examplePartten = ['a', 'a*', '.*', 'c*a*b',
                      'mis*is*p*.', 'mis*is*ip*.', '.*c', 'aaaa', "mis*is*ip*pp*i*i", 'ab*a*c*a', 'ab*']
    ans = [False, True, True, True, False,
           True, False, False, True, True, True]
    for i in range(len(exampleStr)):
        print(isMatch(exampleStr[i], examplePartten[i]), ans[i])
