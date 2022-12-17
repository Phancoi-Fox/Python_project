def longest(str1):
    str_lst = []
    lst = str1.split()
    for i in range(len(lst)):
        str_lst.append(len(lst[i]))
    idx = str_lst.index(max(str_lst))
    return lst[idx]
str1 = input()
print(len(longest(str1)))
