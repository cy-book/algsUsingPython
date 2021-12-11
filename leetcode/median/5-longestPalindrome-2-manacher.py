
class Solution:
    # 求以s[left:right]为中心的子字符串的臂长
    def expand(self, s: str, left, right) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return (right - left - 2) // 2

    def longestPalindrome(self, s: str) -> str:
        s = '#' + '#'.join(s) + '#'
        start, end = 0, -1  # 最长回文串的开始和结束索引
        j = -1  # 中心对称点
        right = -1  # 中心对称点子回文串的右端点
        arm_len = []  # arm_len[i]: 以i为中心，扩展出来的最长子回文串的臂长
        for i in range(len(s)):
            if right >= i:   # 可以利用对称点的臂长
                i_sym = j*2 - i
                # 可利用的臂长局限在 min_arm_len
                min_arm_len = min(arm_len[i_sym], right - i)
                cur_arm_len = self.expand(s, i - min_arm_len, i + min_arm_len)
            else:  # 直接对i进行中心扩展
                cur_arm_len = self.expand(s, i, i)
            arm_len.append(cur_arm_len)
            # 存在问题：无法说明是否可以快速找到最好的中心对称点，它使得计算后来的i的臂长复杂度降到最小
            if i + cur_arm_len > right:  # 替换中心对称点， 特点是中心对称点的臂长可以延伸的更远，让后来的i可以利用前面已经计算了的臂长
                j = i
                right = i + cur_arm_len
            if cur_arm_len * 2 + 1 > end - start:  # 找到更长的回文子串
                end = i + cur_arm_len
                start = i - cur_arm_len
        return s[start + 1:end + 1:2]


if __name__ == '__main__':
    strList = ['babad', 'cbbd', 'a', 'ac']
    results = ['bad', 'bb', 'a', 'a']
    solution = Solution()
    for i in range(len(strList)):
        s = strList[i]
        result = "(" + str(results[i]) + ")"
        sol = str(solution.longestPalindrome(s))
        print(s + ": " + sol + result)
