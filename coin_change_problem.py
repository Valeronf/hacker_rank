coins = [1, 2, 3]

num = [0, 1, 2, 3, 4, 5]

k = [[] for i in range(len(num))]
a = [k for i in range(len(coins))]





print(a)

for i in range(len(coins)):
    for j in range(len(num)):
        if num[j] % coins[i] == 0 and i == 0:
            a[i][j] = 1
        if num[j] % coins[i] == 0 and j != 0 and i != 0:
            a[i][j] = a[i-1][j] + a[i][j-i]