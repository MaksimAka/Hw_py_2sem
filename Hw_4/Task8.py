n = int(input("Кол-во чисел: "))
seq = []
for _ in range(n):
    seq.append(int(input("Число: ")))

print(f"Последовательность: {seq}")

for i in range(len(seq)):
    sub = seq[i:]
    if sub == sub[::-1]:
        to_add = seq[:i][::-1]
        print(f"Нужно приписать чисел: {len(to_add)}")
        print(f"Сами числа: {to_add}")
        break