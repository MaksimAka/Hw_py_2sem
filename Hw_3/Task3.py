count = int(input("Количество видеокарт: "))
cards = []

for i in range(count):
    card = int(input(f"{i + 1} Видеокарта: "))
    cards.append(card)

print("Старый список видеокарт:", cards)

max_card = max(cards)
new_cards = []
for card in cards:
    if card != max_card:
        new_cards.append(card)

print("Новый список видеокарт:", new_cards)