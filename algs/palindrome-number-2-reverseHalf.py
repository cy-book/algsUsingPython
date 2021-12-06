'''
参考：https://leetcode-cn.com/problems/palindrome-number/solution/hui-wen-shu-by-leetcode-solution/

翻转一半数字进行判断，将时间复杂度降到了对数
'''

# date: 2021-12-06


def isPalindrome(x: int) -> bool:
    if (x < 0) or (x % 10 == 0 and x != 0):  # 排除特殊情况
        return False
    reverseNumber = 0
    # x > reverseNumber 也可能已经翻转了一半
    while x > reverseNumber:    # x <= reverseNumber 表示已经翻转了一半数字，或者一半多出一个（奇数个位数则reverseNumber的位数比x多一位）
        digit, x = x % 10, x // 10
        reverseNumber = reverseNumber * 10 + digit
    return reverseNumber == x or x == reverseNumber // 10  # 去除中间位置的那个数，它对判断回文没有影响


if __name__ == '__main__':
    exampleList = [-121, 121, 12, 101, 1]
    ansList = [False, True, False, True, True, True]
    for i in range(len(exampleList)):
        results = isPalindrome(exampleList[i])
        print(exampleList[i], results, '(', ansList[i], ')')
