'''
参考：https://leetcode-cn.com/problems/container-with-most-water/solution/sheng-zui-duo-shui-de-rong-qi-by-leetcode-solution/

双指针解决（贪心算法）
'''

# date: 2021-12-08
# author: cy-book


def maxArea(height: list[int]) -> int:
    n = len(height)
    l, r = 0, n-1
    area = 0
    maxh = max(height)
    while(l < r):
        area = max(area, min(height[l], height[r]) * (r - l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
        # 神之一手
        if area >= maxh * (r - l):
            break
    return area
