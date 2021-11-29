'''
高次幂取模: 求 a^n % b
模运算规律
(a + b) % c = (a % c + b % c) % c
(a - b) % c = (a % c - b % c) % c
(a * b) % c = (a % c * b % c) % c
(a ^ b) % c = ((a % c) ^ b) % c
'''


class Solution:
    def fastPower(self, x: int, n: int, b: int):
        ans = x
        m = x % b
        while n >= 1:
            ans = ans * m
            n -= 1
        return ans % b


if __name__ == '__main__':
    solution = Solution()
    ns = [[2, 31, 3], [3, 23, 5], [33, 44, 22]]
    for n in ns:
        print(n[0], ' ** ', n[1], ' % ', n[2], ' = ',
              solution.fastPower(n[0], n[1], n[2]), '(', n[0] ** n[1] % n[2], ')')
