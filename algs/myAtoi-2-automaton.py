'''
参考：https://leetcode-cn.com/problems/string-to-integer-atoi/solution/zi-fu-chuan-zhuan-huan-zheng-shu-atoi-by-leetcode-/
'''
# date: 2021-12-06


INT_MAX = 2**31 - 1
INT_MIN = -  2**31


class Automaton:
    def __init__(self):
        self.sign = 1
        self.ans = 0
        self.state = 'start'
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end']
        }

    def get_col(self, c: str) -> int:
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c: str):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign else min(
                self.ans, - INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1


def myAtoi(s: str) -> int:
    automaton = Automaton()
    for c in s:
        automaton.get(c)
    return automaton.ans * automaton.sign


if __name__ == '__main__':
    examples = ['123', '234', '+456', '-134',
                '   356adb', '  -423dd3', ' -42', '']
    results = [123, 234, 456, -134, 356, -423, -42, 0]
    for i in range(len(examples)):
        ans = myAtoi(examples[i])
        print(examples[i], ans, '(', results[i], ')')
