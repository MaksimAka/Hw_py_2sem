num_containers = int(input("Количество контейнеров: "))
containers = []

for _ in range(num_containers):
    while True:
        weight = int(input("Введите вес контейнера: "))
        if weight <= 200:
            containers.append(weight)
            break

while True:
    new_weight = int(input("Введите вес нового контейнера: "))
    if new_weight <= 200:
        break

position = 1
for weight in containers:
    if weight >= new_weight:
        position += 1
    else:
        break

print("Номер, который получит новый контейнер:", position)