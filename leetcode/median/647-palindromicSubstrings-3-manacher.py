'''
manacher
'''


class Solution:
    def expand(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 得到的最长回文串为 s[left+1, right-1], 长度必然为奇数
        return (right - left - 2) // 2

    def countSubstrings(self, s: str) -> int:
        s = '#' + '#'.join(s) + '#'  # 扩充字符可以免去奇偶中心字符串的差别，偶字符以扩充字符为中心
        ans = 0
        arm_len = []
        right = -1
        j = 0
        for i in range(len(s)):
            if right <= i:
                cur_arm_len = self.expand(s, i, i)
            else:
                i_sym = j * 2 - i
                min_arm_len = min(arm_len[i_sym], right - i)
                cur_arm_len = self.expand(s, i - min_arm_len, i + min_arm_len)
            arm_len.append(cur_arm_len)
            if right < i + cur_arm_len:
                j = i
                right = i + cur_arm_len
            # 求回文串个数，向上取整（因expand 得到的结果为 奇数 /2 ， 有舍去）
            ans += (arm_len[i] + 1) // 2
        return ans


if __name__ == '__main__':
    strs = ['abc', 'aaa', '', 'a', 'aa', 'fdsklf', 'aaaa', 'aaaaa']
    results = [3, 6, 0, 1, 3, 6, 10, 15]
    solution = Solution()
    for i in range(len(strs)):
        print(strs[i], ": ", solution.countSubstrings(
            strs[i]), '(', results[i], ')')
