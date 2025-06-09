# Angela Yu's 100 Days of Code Challenge - Day 21/22
# Scoreboard Class - Manages score display and game over messages
# Tracks player progress and displays text information on screen

# IMPORTS - Import turtle graphics for text display
from turtle import Turtle

# CONSTANTS - Define text formatting and positioning
ALIGNMENT = "center"                    # Centre-align all text on screen
FONT = ("Courier", 24, "normal")       # Font family, size, and style for text

class Scoreboard(Turtle):
    """Scoreboard class handles score tracking and text display"""

    def __init__(self):
        """CONSTRUCTOR - Set up scoreboard appearance and initial state"""
        super().__init__()          # Inherit all Turtle class methods
        self.score = 0              # Initialize player score to zero
        self.color("white")         # Set text color to white (visible on black background)
        self.penup()               # Lift pen to prevent drawing lines when moving
        self.goto(0, 270)          # Position scoreboard at top centre of screen
        self.hideturtle()          # Hide turtle cursor (only show text)
        self.update_scoreboard()   # Display initial score of 0

    def update_scoreboard(self):
        """UPDATE DISPLAY - Write current score on screen"""
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)  # Display formatted score

    def game_over(self):
        """GAME OVER MESSAGE - Display end game text in centre of screen"""
        self.goto(0, 0)             # Move to centre of screen
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)  # Display game over message

    def increase_score(self):
        """INCREASE SCORE - Add one point and update display"""
        self.score += 1             # Add 1 to current score
        self.clear()               # Clear previous score text from screen
        self.update_scoreboard()   # Display updated score

# SCOREBOARD MECHANICS EXPLANATION:
# Scoreboard displays at top of screen showing current score
# Score increases by 1 each time snake eats food
# When game ends, "GAME OVER" appears in centre of screen
# Text is white colored for visibility against black background
# Turtle cursor is hidden so only text is visible