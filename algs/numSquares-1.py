# description:
#   完全平方数： 给定一个数 n ， 求出最少几个完全平方的和为n.
#   动态规划  f[n] = f[n - i*i] + 1


def isPerfectSquart(n):
    f = [0 for x in range(0, n + 1)]
    for i in range(1, n + 1):
        minn = 10000
        j = 1
        while (j * j <= i):
            minn = min(minn, f[i - j * j])
            j = j + 1
        f[i] = minn + 1
    return f[n]


if __name__ == '__main__':
    for i in range(1000):
        print(isPerfectSquart(i))
