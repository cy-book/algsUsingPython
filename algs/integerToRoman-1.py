'''
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给你一个整数，将其转为罗马数字。

'''


def intToRoman(num: int) -> str:
    romanSet = ['M', 'CM', 'D', 'CD', 'C', 'XC',
                'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    results = ""
    valueTable = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    ''' mul
    for i in range(13):
        n = num // valueTable[i]
        num = num - n * valueTable[i]
        results += (n * romanSet[i])
    '''
    # sub
    for i in range(13):
        while num >= valueTable[i]:
            results += romanSet[i]
            num -= valueTable[i]
    return results


if __name__ == '__main__':
    nums = [3, 4, 9, 58, 1994]
    ans = ["III", "IV", "IX", "LVIII", "MCMXCIV"]
    for i in range(len(nums)):
        results = intToRoman(nums[i])
        print(nums[i], results, ans[i])
