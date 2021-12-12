'''
动态规划
f[i][j] = (连加 (k)(0--(i-1))) f[k][j-1]combinations[i][k]
参考： https://leetcode-cn.com/problems/poor-pigs/solution/
'''


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets == 1:
            return 0
        combinations = [[0] * (buckets + 1)
                        for _ in range(buckets + 1)]  # 计算组合数，i头小猪，选k头的选法
        combinations[0][0] = 1
        iterations = minutesToTest // minutesToDie    # 计算总轮数
        # 计算函数 f ，f(k,j) = k头小猪，j轮可确定多少瓶水里有毒
        # 0头猪 或者 零轮 最多确定一瓶
        # 小猪的数量最多为 buckets - 1头
        f = [[1] * (iterations + 1)] + [[1] + [0] *
                                        iterations for _ in range(buckets - 1)]
        for i in range(1, buckets):  # 猪的个数在 0 - buckets-1 之间， 从最少的开始规划
            # 计算 f 函数的同时计算组合数
            combinations[i][0] = 1
            for j in range(1, buckets):
                combinations[i][j] = combinations[i-1][j] + \
                    combinations[i-1][j-1]
            combinations[i][i] = i
            # 计算 j 轮 k 头猪可以确定瓶子的个数（最底层为 f[i][0] = 1)
            for j in range(1, iterations + 1):
                for k in range(i + 1):
                    #########状态转移方程#########
                    f[i][j] += f[k][j-1] * combinations[i][i - k]
            if f[i][iterations] > buckets:
                return i
        return 0


if __name__ == '__main__':
    solution = Solution()
    minutesToDieList = [15, 15, 15]
    minutesToTestList = [60, 15, 30]
    bucketsList = [1000, 4, 4]
    for i in range(len(bucketsList)):
        print('minutesToDie: ', minutesToDieList[i], ', ', 'minutesToTest: ', minutesToTestList[i], ', ', 'buckets: ',
              bucketsList[i], ', ', 'big: ', solution.poorPigs(bucketsList[i], minutesToDieList[i], minutesToTestList[i]))
