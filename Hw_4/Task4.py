guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print(f"\nСейчас на вечеринке {len(guests)} человек: {guests}")
    action = input("Гость пришел или ушел? ")

    if action == "Пора спать":
        print("Вечеринка закончилась, все легли спать.")
        break

    if action == "пришел":
        name = input("Имя гостя: ")
        if len(guests) < 6:
            print(f"Привет, {name}!")
            guests.append(name)
        else:
            print(f"Прости, {name}, но мест нет.")

    elif action == "ушел":
        name = input("Имя гостя: ")
        if name in guests:
            guests.remove(name)
        print(f"Пока, {name}!")