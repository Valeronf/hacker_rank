num = [0, 1]

coins = [48, 6, 34, 50, 49, 36, 30, 35, 40, 41, 17, 43, 39, 13, 4, 20, 19, 2, 46, 7, 38, 33, 28, 18, 21]

k = [None for i in range(len(num))]
a = [k[:] for i in range(len(coins))]






for i in range(len(coins)):
    for j in range(len(num)):
        if num[j] % coins[i] == 0 and i == 0:
            a[i][j] = 1
            continue
        if num[j] % coins[i] != 0 and i == 0:
            a[i][j] = 0
            continue
        if j == 0:
            a[i][j] = 1
            continue
        if num[j] >= coins[i] and j != 0 and i != 0:
            ind = num[j] - coins[i]
            a[i][j] = a[i-1][j] + a[i][ind]
            continue
        if num[j] < coins[i] and i != 0:
            a[i][j] = a[i - 1][j]
print(a)

