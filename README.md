# GTA-69: A Multiplayer Snake Game

## Description
GTA-69 is a multiplayer snake game built using Python and the Pygame library. The game features two snakes that can be controlled separately and must compete to eat food while avoiding the edges of the screen. The game includes teleportation mechanics at screen boundaries and a scoring system.

## Features
- Two-player support with independent snake controls.
- Randomly spawning food that increases the snake's length.
- Teleportation at screen edges.
- Real-time scoring display.
- Reset functionality for restarting the game.

## Requirements
Ensure you have Python installed along with the Pygame library.

Install Pygame if not already installed:
```sh
pip install pygame
```

## How to Play
- **Player 1 Controls (Arrow Keys):**
  - `↑` (Up Arrow) - Move Up
  - `↓` (Down Arrow) - Move Down
  - `←` (Left Arrow) - Move Left
  - `→` (Right Arrow) - Move Right

- **Player 2 Controls (WASD Keys):**
  - `W` - Move Up
  - `S` - Move Down
  - `A` - Move Left
  - `D` - Move Right

- Press `Enter` to reset the game.
- The game ends when the user closes the window.

## Running the Game
Clone the repository and run the script:
```sh
git clone https://github.com/yourusername/GTA-69.git
cd GTA-69
python game.py
```

## Gameplay Mechanics
- The snakes move continuously in the direction they last moved.
- If a snake eats the food, it grows longer, and the player's score increases.
- Food respawns at a random location after being eaten.
- If a snake reaches the screen boundary, it teleports to the opposite side.

## Notes
- The game uses a predefined frame rate (`fps = 15`) to control movement speed.
- The game screen is 1200x800 pixels.
- The game window displays the scores of both players.

## Future Enhancements
- Adding obstacles for increased difficulty.
- Implementing a game-over condition when a snake collides with itself.
- Enhancing the UI with more graphics and animations.
- Adding sound effects.

## Contributing
Feel free to fork the repository, make improvements, and submit pull requests.

## License
This game is open-source. Feel free to modify and distribute it as needed.

