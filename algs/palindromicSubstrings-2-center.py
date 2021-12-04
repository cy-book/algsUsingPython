'''
中心扩展
与上一种解法的相同想法就是 根据已经找到的子回文字符串 去判断 更大的字符串
而遍历的顺序决定了是否需要记录已经判断过的子字符串


参考： https://leetcode-cn.com/problems/palindromic-substrings/solution/hui-wen-zi-chuan-by-leetcode-solution/
'''


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(2 * n - 1):
            # l, r 的意义:
            # 中心扩展的中心共 2 * n - 1 个， 奇数个元素组成的中心 和 偶数个元素组成的中心
            # 交替计算 奇数 中心 和 偶数中心
            l = i // 2
            r = l + i % 2
            while l >= 0 and r < n and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
        return ans


if __name__ == '__main__':
    strs = ['abc', 'aaa', '', 'a', 'aa', 'fdsklf', 'aaaa', 'aaaaa']
    results = [3, 6, 0, 1, 3, 6, 10, 15]
    solution = Solution()
    for i in range(len(strs)):
        print(strs[i], ": ", solution.countSubstrings(
            strs[i]), '(', results[i], ')')
