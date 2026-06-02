import os

WIN_SCORE = 3
RULES = {"камень": "ножницы", "ножницы": "бумага", "бумага": "камень"}


class Player:

    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""

    def choose_move(self):
        while True:
            move = (
                input(f"{self.name}, выбери (камень, ножницы, бумага): ")
                .lower()
                .strip()
            )
            if move in RULES:
                self.choice = move
                return
            print("Некорректный ввод. Попробуйте еще раз.")


class RockPaperScissors:

    def __init__(self):
        self.p1 = Player("Игрок 1")
        self.p2 = Player("Игрок 2")

    def play_round(self, round_num):
        print(f"=== РАУНД {round_num} ===")
        print(
            f"Текущий счет: {self.p1.name} [{self.p1.points}] : [{self.p2.points}] {self.p2.name}\n"
        )

        self.p1.choose_move()

        input(
            "\nХод записан. Передайте управление второму игроку и нажмите Enter..."
        )
        print("\n"*50)
        print(f"=== РАУНД {round_num} ===\n")

        self.p2.choose_move()

        print("=== РЕЗУЛЬТАТЫ РАУНДА ===")
        print(f"{self.p1.name} выбрал: {self.p1.choice}")
        print(f"{self.p2.name} выбрал: {self.p2.choice}\n")

        if self.p1.choice == self.p2.choice:
            print("Ничья в раунде!")
        elif RULES[self.p1.choice] == self.p2.choice:
            self.p1.points += 1
            print(f"Раунд выиграл {self.p1.name}!")
        else:
            self.p2.points += 1
            print(f"Раунд выиграл {self.p2.name}!")

        input("\nНажмите Enter, чтобы продолжить...")

    def start_game(self):
        round_number = 1

        while self.p1.points < WIN_SCORE and self.p2.points < WIN_SCORE:
            self.play_round(round_number)
            round_number += 1

        print("=== ИГРА ОКОНЧЕНА ===")
        winner = self.p1 if self.p1.points == WIN_SCORE else self.p2
        print(
            f"Победитель: {winner.name} со счетом {self.p1.points}:{self.p2.points}!"
        )


if __name__ == "__main__":
    game = RockPaperScissors()
    game.start_game()
