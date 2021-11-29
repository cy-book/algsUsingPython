class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        s = 1
        h = num
        while s <= h:
            med = (s + h)//2
            sq = med * med
            if sq > num:
                h = med - 1
            elif sq < num:
                s = med + 1
            else:
                return True
        return False


if __name__ == '__main__':
    nums = [1, 12, 8, 0, 16, 18, 36]
    solution = Solution()
    for i in nums:
        print(i, 'is perfect square:', solution.isPerfectSquare(i))
