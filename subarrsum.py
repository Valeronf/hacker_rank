def maxSubarray(arr):
    # Write your code here
    s2 = 0
    for i in arr:
        if i > 0:
            s2 += i
    if s2 == 0 and arr:
        return max(arr), max(arr)
    s_l = 0


    li = []
    for i in arr:
        s_l += i
        if s_l < 0:
            s_l = 0
        li.append(s_l)



    s_f1 = max(li)
    return s_f1, s2