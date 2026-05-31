skates_count = int(input("Кол-во коньков: "))
skates = []
for i in range(skates_count):
    skates.append(int(input(f"Размер {i + 1}-й пары: ")))

people_count = int(input("Кол-во людей: "))
feet = []
for i in range(people_count):
    feet.append(int(input(f"Размер ноги {i + 1}-го человека: ")))

skates.sort()
feet.sort()

match_count = 0
skate_idx = 0
foot_idx = 0

while skate_idx < len(skates) and foot_idx < len(feet):
    if skates[skate_idx] >= feet[foot_idx]:
        match_count += 1
        skate_idx += 1
        foot_idx += 1
    else:
        skate_idx += 1

print(f"Наибольшее кол-во людей, которые могут взять ролики: {match_count}")