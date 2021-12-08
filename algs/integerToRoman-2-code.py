'''
利用编码
参考： https://leetcode-cn.com/problems/integer-to-roman/solution/zheng-shu-zhuan-luo-ma-shu-zi-by-leetcod-75rs/
'''
THOUSANDS = ["", "M", "MM", "MMM"]
HUNDREDS = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
TENS = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
ONES = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]


def intToRoman(self, num: int) -> str:
    return THOUSANDS[num // 1000] + \
        HUNDREDS[num % 1000 // 100] + \
        TENS[num % 100 // 10] + \
        ONES[num % 10]
