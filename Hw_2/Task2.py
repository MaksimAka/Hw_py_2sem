def get_sum(n):
    total_sum = 0
    while n > 0:
        total_sum += n % 10
        n //= 10
    return total_sum

def get_count(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

num = int(input("Введите число: "))

s = get_sum(num)
c = get_count(num)
diff = s - c

print(f"\nСумма чисел: {s}")
print(f"Количество цифр в числе: {c}")
print(f"Разность суммы и количества цифр: {diff}")