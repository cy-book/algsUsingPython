'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

brute force algorithm:
    reverse inteeger using reverse string
'''


def reverse(x: int) -> int:
    strx = str(x)
    if strx[0] == '-':
        smb = '-'
        strx = strx[1:len(strx)]
    else:
        smb = '+'
    n = len(strx)
    newStr = list()
    for i in range(n):
        newStr.append(strx[n - i - 1])
        val = int(''.join(newStr))
        if val > 2 ** 31 or val < 2 ** 31:
            return 0
    return val if smb == '+' else -val


if __name__ == '__main__':
    integerList = [123, -123, -120, 0]
    resultsList = [321, -321, -21, 0]
    for i in range(len(integerList)):
        results = resultsList[i]
        val = integerList[i]
        ans = reverse(val)
        print(val, ": ", ans, '(', results, ')')
