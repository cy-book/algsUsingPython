'''
给你两个字符串 s 和 goal ，只要我们可以通过交换 s 中的两个字母得到与 goal 相等的结果，就返回 true ；否则返回 false 。

交换字母的定义是：取两个下标 i 和 j （下标从 0 开始）且满足 i != j ，接着交换 s[i] 和 s[j] 处的字符。

例如，在 "abcd" 中交换下标 0 和下标 2 的元素可以生成 "cbad" 。

思路：
    判断长度，
    判断是否相同，
        相同则应有两个不同位置的字符相同
        不同则应有两个位置不同，且交换位置后相同
'''


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        l1 = len(s)
        l2 = len(goal)
        if l1 != l2:
            return False
        cnt = 0
        dic = dict()
        dif = [0] * l1
        for i in range(l1):
            dic[s[i]] = 0
        for i in range(l1):
            if s[i] != goal[i]:
                cnt += 1
                dif[i] = 1
            dic[s[i]] += 1
        if cnt == 2:
            x1 = [0] * 2
            x2 = [0] * 2
            ind = 0
            for i in range(l1):
                if dif[i] == 1:
                    x1[ind] = s[i]
                    x2[ind] = goal[i]
                    ind += 1
            if x1[0] == x2[1] and x1[1] == x2[0]:
                return True
            else:
                return False
        if cnt != 0:
            return False
        return max(dic.values()) >= 2


if __name__ == '__main__':
    sList = ['ab', 'ab', 'aa', 'aaaaaaaabc', 'abcaa', 'aaabc']
    goalList = ['ba', 'ab', 'aa', 'aaaaaaaacb', 'abcbb', 'aaacb']
    solution = Solution()
    for i in range(len(sList)):
        print(sList[i], " ,", goalList[i], ": ",
              solution.buddyStrings(sList[i], goalList[i]))
