from collections import deque
from heapq import heappop, nlargest, nsmallest, heapify

# unpacking a sequence into separate variables
# using _
data = ['wang', 21, (2001, 4, 1), 71, 180]
name, age, brithday, _, _ = data
print(name, age, brithday)

# unpacking elements from iterables of arbitrary length
# using *, *_
name, age, *other = data
print(name, other)
name, *_ = data
vals = [1, 2, 3, 4, 5, 6, 7]


def sum_(vals: list[int]):
    head, *tail = vals
    return head + sum_(tail) if tail else head


print(sum_(vals))


# keeping the last n items
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


with open(r'/tmp/base.vim') as f:
    for line, previous_lines in search(f, 'highlight', 1):
        for pline in previous_lines:
            print(pline, end=' ')
        print(line, end=' ')
        print('-'*20)


# finding the largest or smallest n items
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(nlargest(3, nums))  # Prints [42, 37, 23]
print(nsmallest(3, nums))  # Prints [-4, 1, 2]
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = nlargest(3, portfolio, key=lambda s: s['price'])
print(cheap)
print(expensive)
heapify(nums)   # 堆排序， 优先队列
print(nums)
n = len(nums)
for i in range(n):
    print(heappop(nums))
