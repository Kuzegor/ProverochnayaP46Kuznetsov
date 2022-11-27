j = 0
i = 1
n = 5
while n < 10:
    n2 = n
    while j < i:
        print(n2, end='');
        j += 1
        n2 -= 1
    j = 0
    n += 1
    i += 1
    print()
