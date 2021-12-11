'''
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。

思路： 遍历可能的情况，在一些特殊位置设置标签，可以减少一定的计算
'''

# date: 2021-12-08
# author: cy-book


def maxArea(height: list[int]) -> int:
    n = len(height)
    area = 0
    maxR = 0
    for r in range(n-1, 0, -1):
        if height < maxR:
            continue
        maxL = 0
        for l in range(maxL, r):
            if height[l] > maxL:
                temp = (min(height[l], height[r]) * (r - l))
                if temp > area:
                    maxL = height[l]
                    maxR = height[r]
                    area = temp
    return area
