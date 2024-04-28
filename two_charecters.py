
s = 'asdcbsdcagfsdbgdfanfghbsfdab'
d = True
while (d and s):
    for i in range(len(s)):
        if i < len(s) - 1:
            if s[i] == s[i + 1]:
                s = s.replace(s[i], '')
                d = True
                break
        else:
            d = False




res = s


print(res)
ans = []
while len(res) > 2:
    i = 0
    k_s = 0
    numer = 1
    lis = []
    for j in range(i + 1, len(res)):
        if res[j] == res[k_s]:
            lis.append(res[k_s + 1:j])
            k_s = j
            numer += 1
    if k_s != len(res) - 1:
        lis.append(res[k_s + 1:])

    for i in range(len(lis)):
        dic = {}
        for j in lis[i]:
            if j not in dic:
                dic[j] = 1
            else:
                lis[i] = lis[i].replace(j, '')
    print(lis)
    dic2 = {}
    for i in lis:
        for j in i:
            if j not in dic2:
                dic2[j] = 1
            else:
                dic2[j] += 1
    print(dic2)
    v_lis = list(dic2.values())
    v_lis.sort(reverse=True)
    print(v_lis)
    if v_lis[0] < numer - 1 or numer+v_lis[0] < 3 or v_lis[0] < len(lis):
        ans.append(0)
    else:
        ans.append(numer+v_lis[0])
    res = res[1:]


print(ans)





