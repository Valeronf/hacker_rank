s = 'beabeefeab'


for i in range(len(s)):
    if i < len(s) - 1:
        if s[i] == s[i + 1]:
            res = s.replace(s[i], '')

for i in range(len(res) - 1):
    k_s = 0
    lis = []
    for j in range(i + 1, len(res)):
        if res[j] == res[k_s]:
            lis.append(res[k_s + 1:j])
            k_s = j

