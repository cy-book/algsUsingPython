'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
'''

# date:2021-12-12
# author: cy-book

parenthesisMap = {
    '{': '}',
    '(': ')',
    '[': ']'
}


def isValid(s: str) -> bool:
    stack = list()
    for ch in s:
        if ch in '({[':
            stack.append(ch)
        else:
            if stack and parenthesisMap[stack.pop()] == ch:
                continue
            else:
                return False
    return True if not stack else False
