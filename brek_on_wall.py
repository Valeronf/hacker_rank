import math

n = 4
m = 5

lis = []
def comb(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

for i in range(m - 1, 0, -1):
    k = ((m - 1) - i) * n
    su = 0
    for j in range(k + 1):
        su += comb(k, j)
    lis.append(su)
print(lis)
for i in range(len(lis)):
    ind = lis[i] * (i + 1)
    for j in range(i + 1, len(lis)):
        lis[j] -= ind
print(lis)
for i in range(0,len(lis)):
    lis[i] = comb(len(lis), len(lis) - i) * lis[i]
print(lis)
ans = (2 ** (m - 1)) ** n - sum(lis)
print(ans)
