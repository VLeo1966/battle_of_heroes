from hero import Hero
from game import Game

if __name__ == "__main__":
    player_name = input("Введите имя вашего героя: ")
    player = Hero(player_name)
    computer = Hero("Компьютерный герой")

    game = Game(player, computer)
    game.start()
