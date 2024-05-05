def alternate(s):
    # Write your code here
    if len(s) == 1:
        return 0
    if len(s) == 2 and s[0] == s[1]:
        return 0
    if len(s) == 2 and s[0] != s[1]:
        return 2

    def del_dop(s):
        for i in range(len(s)):
            if i < len(s) - 1:
                if s[i] == s[i + 1]:
                    s = s.replace(s[i], '')
                    return del_dop(s)
            if i == len(s) - 1:
                return s
    res = del_dop(s)
    if not res:
        return 0

    ans = []
    while (res and len(res) > 2):
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
        lis_mem = []
        for i in range(len(lis)):
            dic = {}
            for j in lis[i]:
                if j not in dic:
                    dic[j] = 1
                else:
                    lis_mem.append(j)
                    lis[i] = lis[i].replace(j, '')


        if lis_mem and lis:
            for i in lis_mem:
                for j in range(len(lis)):
                    if i in lis[j]:
                        lis[j] = lis[j].replace(i, '')

        dic2 = {}
        for i in lis:
            for j in i:
                if j not in dic2:
                    dic2[j] = 1
                else:
                    dic2[j] += 1

        v_lis = list(dic2.values())
        v_lis.sort(reverse=True)
        if v_lis:
            ind = 0
            if len(lis) > 1:
                st = lis[:len(lis) - 1]
                if st:
                    inter = set(st[0])
                    for stri in st[1:]:
                        inter &= set(stri)
                    if not inter:
                        ind = 1
                    if set(inter) & set(lis_mem):
                        ind = 1
            if v_lis[0] < numer - 1 or numer+v_lis[0] < 3:
                ans.append(0)
                ind = 1
            elif ind != 1:
                ans.append(numer+v_lis[0])
            res = res.replace(res[0], '')
            res = del_dop(res)
        else:
            res = res.replace(res[0], '')
            res = del_dop(res)

    ans.sort(reverse=True)
    if ans:
        return ans[0]
    else:
        return 0