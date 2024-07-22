# lesson11
 create game using kanban of method

# Battle of Heroes

Battle of Heroes is a simple console-based text battle game where the player and the computer each control a hero with different attributes. The game consists of rounds where players take turns attacking each other until one hero's health reaches zero.

## Features

- Object-Oriented Programming (OOP) design.
- Simple console-based gameplay.
- Heroes with customizable names, health, and attack power.

## Classes

### Hero

- **Attributes:**
  - `name`: The name of the hero.
  - `health`: The health of the hero, default value is 100.
  - `attack_power`: The attack power of the hero, default value is 20.

- **Methods:**
  - `attack(other)`: Attacks another hero, reducing their health by the hero's attack power.
  - `is_alive()`: Returns `True` if the hero's health is greater than 0, otherwise `False`.

### Game

- **Attributes:**
  - `player`: An instance of the `Hero` class representing the player.
  - `computer`: An instance of the `Hero` class representing the computer.

- **Methods:**
  - `start()`: Starts the game, alternating turns between the player and the computer until one of the heroes dies. Outputs information about each turn and declares the winner.
  - `display_health()`: Displays the current health of both the player and the computer.

## How to Run

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/battle_of_heroes.git
    ```

2. Navigate to the project directory:
    ```sh
    cd battle_of_heroes
    ```

3. Run the game:
    ```sh
    python main.py
    ```

4. Follow the on-screen prompts to play the game.

## Project Structure

<<<<<<< HEAD
|-- hero.py # Contains the Hero class

|-- game.py # Contains the Game class

|-- main.py # The main script to run the game

|-- README.md # This README file
=======
battle_of_heroes/
|-- hero.py # Contains the Hero class
|-- game.py # Contains the Game class
|-- main.py # The main script to run the game
|-- README.md # This README file

## Future Enhancements

- Add more hero attributes such as defense, agility, etc.
- Implement special abilities for heroes.
- Create a more advanced AI for the computer opponent.
- Develop a graphical user interface (GUI) for the game.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

>>>>>>> 2bed097049512927beee1f516c781fe89c31489f
