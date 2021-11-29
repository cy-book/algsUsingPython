'''
四数成绩
给定一个长度为n的数组a 和 一个正整数k，从数组中选择四个数，要求四个数的乘积小于等于k
求总方案个数

思路： 折半枚举， 容斥定理    O(n^4)  ->  O(n^2)
参考： https://www.lintcode.com/problem/1441/
'''


class Solution:
    def numofplan(self, n: int, a: list, k: int) -> int:
        cnt = [0] * 10010
        sum = [0] * 10010
        for i in range(n):
            if a[i] > k:
                continue
            else:
                cnt[a[i]] += 1
        for i in range(n):
            for j in range(i+1, n):
                if a[i] * a[j] > k:
                    continue
                else:
                    sum[a[i] * a[j]] += 1
        for i in range(1, k+1):
            cnt[i] += cnt[i - 1]  # cnt[i] 表示数组中有多少个数小于i
            sum[i] += sum[i - 1]  # sum[i] 表示数组中有多少对不重复的数，其乘积小于i
        ans = 0
        for i in range(n):
            for j in range(i+1, n):  # 双重循环枚举任意两个数
                res1 = a[i] * a[j]
                if res1 > k:
                    continue
                res = k // res1
                ans += sum[res]     # res1 < k 则可存在 res 与之配对，有sum[res]个
                # 在组成res的任意两个数中，有包含 a[i]的部分， 舍去
                # 包含a[i] 的部分有 cnt[res // a[i]]
                # 即对于当个这个a[i], 有res//a[i] 可以与他结合成 res, 有cnt[res//a[i]] 个
                if a[i] <= res:
                    ans -= cnt[res // a[i]]
                    # 如果 a[i] <= res // a[i] ，则有 a[i] * a[i] <= res
                    # 表示 cnt[res/a[i]] 个小于res/a[i] 的数中也有 a[i] 自己， 但本身sum并没有计算a[i] * a[i] 这一项（不能重复选择）
                    # 所以在 ans -= cnt[res // a[i]] 时多删除了一个结果， 现在加回来
                    if a[i] <= res // a[i]:
                        ans += 1
                if a[j] <= res:
                    ans -= cnt[res // a[j]]
                    if a[j] <= res // a[j]:
                        ans += 1
                if a[j] * a[i] <= res:   # a[j] 与 a[i] 同时构成 res时会被重复减去
                    ans += 1
        return ans // 6  # 对于每一个答案四元组， 每次枚举两个， 会重6次


if __name__ == '__main__':
    ns1 = [1, 1, 1, 2, 2]
    ns2 = [2, 4, 9, 4, 3]
    solution = Solution()
    print(ns1, ": ", solution.numofplan(5, ns1, 3))
    print(ns2, ": ", solution.numofplan(5, ns2, 300))
