lst = [1, 4, -3, 0, 10, 15, 22, 7, 8]

for i in range(len(lst) - 1, -1, -1):
    if lst[i] % 2 == 0:
        print(lst[i], end=" ")
print()