n = int(input("Кол-во человек: "))
k = int(input("Какое число в считалке? "))
print(f"Значит, выбывает каждый {k}-й человек")

people = list(range(1, n + 1))
start_idx = 0

while len(people) > 1:
    print(f"\nТекущий круг людей: {people}")
    print(f"Начало счета с номера {people[start_idx]}")

    drop_idx = (start_idx + k - 1) % len(people)
    print(f"Выбывает человек под номером {people[drop_idx]}")

    people.pop(drop_idx)

    if drop_idx == len(people):
        start_idx = 0
    else:
        start_idx = drop_idx

print(f"\nОстался человек под номером {people[0]}")