lst = [1, 4, -3, 0, 10]

print("Изначальный список:", lst)

for i in range(len(lst)):
    for j in range(0, len(lst) - i - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print("Отсортированный список:", lst)