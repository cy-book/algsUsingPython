"""
0 < num <= 2^30
判断num 是否为 2^30 的约数来判断 num是否为 2的幂
"""


class Solution:
    def isPowerOfTwo(self, num: int) -> bool:
        return num > 0 and 2**30 % num == 0


if __name__ == '__main__':
    ns = [0, 1, 4, 5, 16, 17]
    solution = Solution()
    for i in ns:
        print(i, 'is power of 2: ', solution.isPowerOfTwo(i))
