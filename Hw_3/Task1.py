N = int(input("Введите число: "))
odd_numbers = []

for i in range(1, N + 1, 2):
    odd_numbers.append(i)

print("Список из нечётных чисел от одного до N:", odd_numbers)