text = input("Введите строку: ")

first_h = text.find("h")
last_h = text.rfind("h")

inside_reversed = text[first_h + 1 : last_h][::-1]

print(
    f"Развернутая последовательность между первым и последним h: {inside_reversed}"
)