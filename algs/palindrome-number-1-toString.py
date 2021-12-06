'''
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。
'''
# date: 2021-12-06
# author: cy-book


def isPalindrome(x: int) -> bool:
    xs = str(x)
    left, right = 0, len(xs)-1
    while left < right:
        if xs[left] != xs[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == '__main__':
    exampleList = [-121, 121, 12, 101, 1]
    ansList = [False, True, False, True, True, True]
    for i in range(len(exampleList)):
        results = isPalindrome(exampleList[i])
        print(exampleList[i], results, '(', ansList[i], ')')
