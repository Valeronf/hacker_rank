# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def stockmax(prices):
    # Write your code here
    s = 0
    while prices:
        m = max(prices)
        k = prices.index(m)
        lis = prices[k + 1:]
        for i in range(k):
            s += prices[k] - prices[i]
        prices = lis
    return s