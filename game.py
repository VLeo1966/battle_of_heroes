import random
from hero import Hero

class Game:
    def __init__(self, player, computer):
        """
        Инициализация игры с игроком и компьютером.
        """
        self.player = player
        self.computer = computer

    def start(self):
        """
        Начинает игру, чередуя ходы игрока и компьютера до тех пор, пока один из них не умрет.
        """
        print("Игра начинается!")
        while self.player.is_alive() and self.computer.is_alive():
            if random.choice([True, False]):
                self.player.attack(self.computer)
            else:
                self.computer.attack(self.player)

            self.display_health()

            if not self.player.is_alive():
                print(f"{self.player.name} пал в бою. {self.computer.name} победил!")
            elif not self.computer.is_alive():
                print(f"{self.computer.name} пал в бою. {self.player.name} победил!")

    def display_health(self):
        """
        Отображает текущее здоровье игрока и компьютера.
        """
        print(f"{self.player.name}: {self.player.health} здоровья")
        print(f"{self.computer.name}: {self.computer.health} здоровья")
