'''
给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。

回文字符串 是正着读和倒过来读一样的字符串。

子字符串 是字符串中的由连续字符组成的一个序列。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。


思路:  如果 xx 是回文字符串， 那么判断 yxxy 是回文字符串的方法就是 判断 y y 是否相同
'''


class Solution:
    def countSubstrings(self, s: str) -> int:
        m = len(s)
        # 认识列表的浅复制 和 初始化， 注释着的这种方法为复制列表， 不同引用指向同一块内存， 会被一块改变值
        # isPalindrome = [[False] * m] * m
        isPalindrome = [[False for _ in range(m)] for _ in range(m)]
        cnt = 0
        for i in range(m - 1):
            isPalindrome[i][i] = True
            cnt += 1
            if s[i] == s[i+1]:
                isPalindrome[i][i+1] = True
                cnt += 1
        if m > 0:
            isPalindrome[m-1][m-1] = True
            cnt += 1

        '''
        使用了三种循环，下面这一种复合解题思路，每次大遍历要遍历每一行，第 n 次遍历要遍历 每一行的 前 n个元素
        '''
        for i in range(2, m):
            for j in range(m):
                e = j + i
                if e >= m:
                    break
                if isPalindrome[j + 1][e - 1] and s[j] == s[e]:
                    isPalindrome[j][e] = True
                    cnt += 1
        return cnt
    '''
        for i in range(m):
            for j in range(2, m):
                e = i + j
                if e >= m:
                    break
                if isPalindrome[i + 1][e - 1] and s[i] == s[e]:
                    isPalindrome[i][e] = True
                    cnt += 1
    '''

    '''
        for i in range(m):
            for j in range(i+2, m):
                if isPalindrome[i+1][j-1] and s[i] == s[j]:
                    isPalindrome[i][j] == True
                    cnt += 1
    '''


if __name__ == '__main__':
    strs = ['abc', 'aaa', '', 'a', 'aa', 'fdsklf', 'aaaa', 'aaaaa']
    results = [3, 6, 0, 1, 3, 6, 10, 15]
    solution = Solution()
    for i in range(len(strs)):
        print(strs[i], ": ", solution.countSubstrings(
            strs[i]), '(', results[i], ')')
