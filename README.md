# 🐍 Snake Game

A classic Snake Game built with Python's Turtle Graphics module! Control the snake to eat food, grow longer, and avoid collisions in this nostalgic arcade experience.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Turtle Graphics](https://img.shields.io/badge/Turtle-Graphics-green?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

## 🎮 Game Features

- 🕹️ **Classic Gameplay** - Navigate your snake to eat food and grow
- 🌈 **Colorful Food** - Random colored food items for visual appeal  
- 📊 **Live Scoring** - Real-time score tracking and display
- ⚡ **Smooth Controls** - Responsive arrow key movement
- 💥 **Collision Detection** - Wall and self-collision game mechanics
- 🎯 **Progressive Difficulty** - Snake gets longer as you eat more food

## 🚀 How to Play

1. **Start the Game** - Run `python main.py`
2. **Control the Snake** - Use arrow keys to move:
   - ⬆️ **Up Arrow** - Move Up
   - ⬇️ **Down Arrow** - Move Down  
   - ⬅️ **Left Arrow** - Move Left
   - ➡️ **Right Arrow** - Move Right
3. **Objective** - Eat the colorful food to grow and increase your score
4. **Avoid** - Don't hit the walls or your own tail!
5. **Exit** - Click anywhere on the screen to close the game

## 🛠️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/qusai-Kagalwala/snake-game.git

# Navigate to project directory
cd snake-game

# Run the game (Python 3.x required)
python main.py
```

> **Note**: This game uses Python's built-in `turtle` module, so no additional packages need to be installed!

## 📁 Project Structure

```
snake-game/
├── main.py         # 🎮 Main game loop and setup
├── snake.py        # 🐍 Snake class (movement, growth, controls)
├── food.py         # 🍎 Food class (random generation, colors)
├── scoreboard.py   # 📊 Scoreboard class (score tracking, display)
└── README.md       # 📖 Project documentation
```

## 🧩 Code Architecture

The game follows **Object-Oriented Programming** principles with four main components:

- **🎯 Main Game Loop** (`main.py`) - Coordinates all game elements and handles the game state
- **🐍 Snake Class** (`snake.py`) - Manages snake creation, movement, growth, and direction controls
- **🍎 Food Class** (`food.py`) - Handles food generation, positioning, and visual variety
- **📊 Scoreboard Class** (`scoreboard.py`) - Tracks and displays the player's score and game over messages

## 🎨 Game Mechanics

- **Movement**: Snake moves continuously in the current direction
- **Food Collision**: When snake head is within 15 pixels of food, score increases and snake grows
- **Wall Collision**: Game ends if snake hits any boundary (±280 pixels)
- **Self Collision**: Game ends if snake head touches any part of its body
- **Speed**: Game runs at 10 FPS with 0.1-second intervals

## 🏆 Learning Outcomes

This project demonstrates:
- ✅ Object-Oriented Programming in Python
- ✅ Game loop implementation
- ✅ Event handling and keyboard input
- ✅ Collision detection algorithms  
- ✅ Graphics programming with Turtle
- ✅ Modular code organization

## 🎓 About

This project is part of **Angela Yu's 100 Days of Code Challenge** (Day 21/22), focusing on building games with Python's Turtle Graphics module.

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for improvements! Some ideas:
- 🎵 Add sound effects
- 🏆 Implement high score system
- 🎨 Add different themes/skins
- ⚙️ Add difficulty levels
- 📱 Mobile-friendly version

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Connect

**Qusai Kagalwala**
- 💼 [LinkedIn](https://www.linkedin.com/in/qusai-kagalwala/)
- 🐙 [GitHub](https://github.com/qusai-Kagalwala)
- 📧 qusai.kagalwala53@gmail.com

---

⭐ **Star this repository if you enjoyed the game!** ⭐
