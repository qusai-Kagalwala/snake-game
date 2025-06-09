# Angela Yu's 100 Days of Code Challenge - Day 21/22
# Snake Game - Classic arcade game using turtle graphics
# Control snake to eat food, grow longer, and avoid walls/tail collision

# IMPORTS - Import required modules and classes
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# SCREEN SETUP - Configure game window and display settings
screen = Screen()                    # Create main game window
screen.setup(width=600, height=600) # Set window size to 600x600 pixels
screen.bgcolor("black")              # Set background colour to black
screen.title("My Snake Game")        # Set window title
screen.tracer(0)                     # Turn off animation for smooth gameplay

# GAME OBJECTS - Create instances of snake, food, and scoreboard
snake = Snake()         # Create snake object (starts with 3 segments)
food = Food()           # Create food object (appears randomly on screen)
scoreboard = Scoreboard() # Create scoreboard object (tracks and displays score)

# KEYBOARD CONTROLS - Set up arrow key controls for snake movement
screen.listen()                     # Tell screen to listen for key presses
screen.onkey(snake.up, "Up")        # Bind Up arrow to snake up movement
screen.onkey(snake.down, "Down")    # Bind Down arrow to snake down movement
screen.onkey(snake.left, "Left")    # Bind Left arrow to snake left movement
screen.onkey(snake.right, "Right")  # Bind Right arrow to snake right movement

# MAIN GAME LOOP - Core game logic that runs continuously
game_is_on = True  # Game state variable to control main loop
while game_is_on:
    screen.update()  # Refresh screen to show latest positions
    time.sleep(0.1)  # Pause for 0.1 seconds to control game speed
    snake.move()     # Move snake forward by one step

    # FOOD COLLISION DETECTION - Check if snake head touches food
    if snake.head.distance(food) < 15:  # If snake head is within 15 pixels of food
        food.refresh()                  # Generate new food at random location
        snake.extend()                  # Add new segment to snake body
        scoreboard.increase_score()     # Add 1 point to player's score

    # WALL COLLISION DETECTION - Check if snake hits any of the four walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False              # End game if wall collision detected
        scoreboard.game_over()          # Display game over message

    # TAIL COLLISION DETECTION - Check if snake head hits its own body
    for segment in snake.segments[1:]:  # Check all segments except head (index 0)
        if snake.head.distance(segment) < 10:  # If head touches any body segment
            game_is_on = False          # End game if tail collision detected
            scoreboard.game_over()      # Display game over message

# PROGRAM EXIT - Keep window open until user clicks to close
screen.exitonclick()  # Wait for mouse click to close game window

# GAME CONTROLS SUMMARY:
# ↑ Arrow = Move Up      ↓ Arrow = Move Down
# ← Arrow = Move Left    → Arrow = Move Right
# Click = Exit Game