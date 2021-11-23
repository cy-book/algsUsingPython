'''
python的lambda表达式
参考： https://leetcode-cn.com/problems/buddy-strings/submissions/
'''


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            if len(set(s)) < len(goal):
                return True
            else:
                return False
        diff = [(a, b) for a, b in zip(s, goal) if a != b]
        return len(diff) == 2 and diff[0][0] == diff[1][1] and diff[0][1] == diff[1][0]


if __name__ == '__main__':
    sList = ['ab', 'ab', 'aa', 'aaaaaaaabc', 'abcaa', 'aaabc']
    goalList = ['ba', 'ab', 'aa', 'aaaaaaaacb', 'abcbb', 'aaacb']
    solution = Solution()
    for i in range(len(sList)):
        print(sList[i], " ,", goalList[i], ": ",
              solution.buddyStrings(sList[i], goalList[i]))
