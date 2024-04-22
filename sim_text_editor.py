ops = ['1 lchbfcjtfpsmjrqsdgci', '3 19', '1 cpcvixlm', '1 apdjgjydvpbpvyiy', '2 29', '4', '4', '3 9', '4', '4']
ans = []
S = ''
n = 10
for i in range(n):
    if ops[i][0] == '1':
        S = S + ops[i][2:]
        ans.append(S)
    if ops[i][0] == '2':
        k = int(ops[i][2:])
        l = len(S)
        S = S[:l - k]
        ans.append(S)
    if ops[i][0] == '3':
        o = int(ops[i][2:]) - 1
        print(S[o])
    if ops[i][0] == '4' and ans:
        ans.pop()
        if len(ans) >= 1:
            u = len(ans) - 1
            S = ans[u]
        else:
            S = ''