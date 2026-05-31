lower_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
upper_alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

message = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))

encrypted_message = ""

for char in message:
    if char in lower_alphabet:
        index = lower_alphabet.index(char)
        new_index = (index + shift) % len(lower_alphabet)
        encrypted_message += lower_alphabet[new_index]
    elif char in upper_alphabet:
        index = upper_alphabet.index(char)
        new_index = (index + shift) % len(upper_alphabet)
        encrypted_message += upper_alphabet[new_index]
    else:
        encrypted_message += char

print(f"Зашифрованное сообщение: {encrypted_message}")