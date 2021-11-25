'''
思路： 滑动窗口，另一种思考方式
参考： https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/wu-zhong-fu-zi-fu-de-zui-chang-zi-chuan-by-leetc-2/
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cSet = set()
        n = len(s)
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                cSet.remove(s[i-1])
            while rk + 1 < n and s[rk + 1] not in cSet:
                rk += 1
                cSet.add(s[rk])
            ans = max(ans, rk + 1 - i)
        return ans


if __name__ == '__main__':
    ss = ['awabcabcbb', 'bbbbbbcd', 'pwwkew', '', ' ', 'abc']
    solution = Solution()
    for s in ss:
        print(s, ': ', solution.lengthOfLongestSubstring(s))
