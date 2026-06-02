import random


class User:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def throw_card(self, action_word="take", can_skip=True):
        prompt = f'{self.name}, выберите карту'
        if can_skip:
            prompt += f' (или введите "{action_word}")'
        prompt += ': '

        while True:
            card = input(prompt)
            if can_skip and card == action_word:
                return action_word
            if card in self.hand:
                self.hand.remove(card)
                return card
            print("Такой карты нет в руке или команда введена неверно!")


class Deck:
    def __init__(self):
        suits = ['Черви', 'Пики', 'Бубны', 'Крести']
        values = ['06', '07', '08', '09', '10', '11', '12', '13', '14']

        self.deck = [f"{v}_{s}" for v in values for s in suits]
        random.shuffle(self.deck)

    def give_card(self):
        if self.deck:
            return self.deck.pop(0)
        return None

    def size(self):
        return len(self.deck)


class Rules:
    def __init__(self, trump):
        self.trump = trump

    def check(self, attack, defend):
        att_val, att_suit = int(attack.split('_')[0]), attack.split('_')[1]
        def_val, def_suit = int(defend.split('_')[0]), defend.split('_')[1]

        if def_suit == att_suit and def_val > att_val:
            return True

        if def_suit == self.trump and att_suit != self.trump:
            return True

        print("Нельзя отбиться этой картой!")
        return False


class Game(Rules):
    def __init__(self):
        self.deck_obj = Deck()

        self.trump_card = self.deck_obj.deck[-1]
        trump_suit = self.trump_card.split('_')[1]

        super().__init__(trump_suit)
        print(f"Козырь игры: {self.trump_card} (Масть: {self.trump})")

    def play(self):
        name1 = input("Игрок 1: ")
        name2 = input("Игрок 2: ")

        hand1 = [self.deck_obj.give_card() for _ in range(6)]
        hand2 = [self.deck_obj.give_card() for _ in range(6)]

        p1 = User(name1, hand1)
        p2 = User(name2, hand2)

        attacker, defender = p1, p2

        while p1.hand and p2.hand:

            for player in [attacker, defender]:
                while len(player.hand) < 6 and self.deck_obj.size() > 0:
                    player.hand.append(self.deck_obj.give_card())

            if not p1.hand or not p2.hand:
                break

            table = []

            print("\n" + "=" * 30)
            print(f"В колоде осталось карт: {self.deck_obj.size()}")
            print(f"Ход: атакует {attacker.name}")
            print("Ваша рука:", ", ".join(attacker.hand))

            attack = attacker.throw_card(can_skip=False)
            table.append(attack)

            print(f"\n{defender.name} отбивается от {attack}")
            print("Ваша рука:", ", ".join(defender.hand))

            while True:
                defend = defender.throw_card(action_word="take", can_skip=True)

                if defend == "take":
                    defender.hand.extend(table)
                    print(f"> {defender.name} забирает карты!")
                    break

                if self.check(attack, defend):
                    table.append(defend)
                    print("> Отбито! (Бито)")
                    attacker, defender = defender, attacker
                    break

        print("\n" + "=" * 30)
        if not p1.hand and not p2.hand:
            print("Игра окончена! Ничья!")
        else:
            winner = p1 if not p1.hand else p2
            print(f"Игра окончена! Победил {winner.name}!")


if __name__ == "__main__":
    game = Game()
    game.play()