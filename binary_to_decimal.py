n_binary = int(input())
dec_value=0
i = 1
length = len(str(n_binary))
for k in range(length):
    reminder = n_binary % 10
    dec_value = dec_value + (reminder * i)
    i = i * 2
    n_binary = int(n_binary/10)
print(dec_value)
