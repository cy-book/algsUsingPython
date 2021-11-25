'''
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
思路： 滑动窗口
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cSet = set()
        l, r = 0, 0
        longestLength = 0
        while r < len(s):
            if s[r] in cSet:
                longestLength = max(longestLength, r-l)
                cSet.remove(s[l])
                l += 1
            else:
                cSet.add(s[r])
                r += 1
        longestLength = max(longestLength, r-l)
        return longestLength


if __name__ == '__main__':
    ss = ['awabcabcbb', 'bbbbbbcd', 'pwwkew', '', ' ', 'abc']
    solution = Solution()
    for s in ss:
        print(s, ': ', solution.lengthOfLongestSubstring(s))
