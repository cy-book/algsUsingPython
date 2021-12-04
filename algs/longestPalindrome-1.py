'''
给你一个字符串 s，找到 s 中最长的回文子串。
'''


class Solution:
    def expand(self, s: str, left: int, right: int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, -1
        for i in range(len(s)):
            left1, right1 = self.expand(s, i, i)
            left2, right2 = self.expand(s, i, i+1)
            if right1 - left1 > end - start:
                end, start = right1, left1
            if right2 - left2 > end - start:
                end, start = right2, left2
        return s[start:end + 1]


if __name__ == '__main__':
    strList = ['babad', 'cbbd', 'a', 'ac']
    results = ['bad', 'bb', 'a', 'a']
    solution = Solution()
    for i in range(len(strList)):
        s = strList[i]
        result = "(" + str(results[i]) + ")"
        sol = str(solution.longestPalindrome(s))
        print(s + ": " + sol + result)
