def get_smallest_divisor(n):
    divisor = 2

    while n % divisor != 0:
        divisor += 1

    return divisor


num = int(input("Введите число: "))

print(f"Наименьший делитель, отличный от единицы: {get_smallest_divisor(num)}")
