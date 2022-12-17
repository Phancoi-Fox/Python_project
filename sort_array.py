n = int(input())
lst = []
for i in range(n):
    m = int(input())
    lst.append(m)
for i in range(0, n-1):
    for j in range(i + 1, n):
        if (abs(lst[i]) < abs(lst[j])):
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp
print(lst)
