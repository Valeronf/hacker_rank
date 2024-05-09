import math
from decimal import Decimal

arr = list([i for i in range(100000, 0, -1)])


curr = 0
for i in arr:
    if i >= curr:
        curr = curr - (i - curr)

if curr < 0:
    curr = curr * (-1)
    step = 2 ** len(arr)
    step = Decimal(step)
    curr = Decimal(curr)

    an = curr/step
    print(an)


