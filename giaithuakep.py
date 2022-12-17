n = int(input())
s = 1
k = 1
if n == 0 or n == 1:
    print(1)
else:
    for i in range(2, n+1):
        if n % 2 == 0:
            if i % 2 == 0:
                s = s*i
        else:
            if i % 2 != 0:
                k = k*i
if n % 2 == 0:
    print(s)
else:
    print(k)
