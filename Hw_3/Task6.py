K = int(input("Сдвиг: "))
lst = [1, 2, 3, 4, 5]

print("Изначальный список:", lst)

K = K % len(lst)
lst = lst[-K:] + lst[:-K]

print("Сдвинутый список:", lst)