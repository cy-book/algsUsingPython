'''
a & (a-1) : 移除a二进制表示的最低位的1
a & (-a)  : 获得a二进制表示的最低位的1的值
'''


class Solution:
    def isPowerOfTwo(self, num: int) -> bool:
        return num > 0 and (num & (num - 1)) == 0


if __name__ == '__main__':
    ns = [0, 1, 4, 5, 16, 17]
    solution = Solution()
    for i in ns:
        print(i, 'is power of 2: ', solution.isPowerOfTwo(i))
