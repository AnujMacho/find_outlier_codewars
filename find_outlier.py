def find_outlier(integers):
    l1 = []
    l2 = []
    for a in integers:
        if a%2==0:
            l1.append(a)
        else:
            l2.append(a)
    if len(l1) == 1: return l1[0]
    return l2[0]

print(find_outlier([2, 4, 0, 100, 4, 39, 2602, 36]))