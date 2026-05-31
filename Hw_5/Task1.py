text = input("Введите текст: ")
vowels = [char for char in text if char.lower() in "ауоиэыяюеё"]

print(f"Список гласных букв: {vowels}")
print(f"Длина списка: {len(vowels)}")