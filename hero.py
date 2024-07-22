class Hero:
    def __init__(self, name, health=100, attack_power=20):
        """
        Инициализация героя с именем, здоровьем и силой атаки.
        """
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        """
        Атакует другого героя, уменьшая его здоровье на значение силы атаки.
        """
        other.health -= self.attack_power
        print(f"{self.name} атаковал {other.name} и нанес {self.attack_power} урона.")

    def is_alive(self):
        """
        Проверяет, жив ли герой (здоровье больше 0).
        """
        return self.health > 0
