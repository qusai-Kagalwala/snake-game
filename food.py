# Angela Yu's 100 Days of Code Challenge - Day 21/22
# Food Class - Manages food generation and appearance
# Creates colorful food items that appear randomly on screen

# IMPORTS - Import required modules for food creation
from turtle import Turtle
import random


class Food(Turtle):
    """Food class inherits from Turtle to create edible items for snake"""

    def __init__(self):
        """CONSTRUCTOR - Set up food appearance and initial position"""
        super().__init__()  # Inherit all Turtle class methods
        self.shape("circle")  # Set food shape to circle
        self.penup()  # Lift pen to prevent drawing lines
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Make food smaller (half size)
        self.speed("fastest")  # Set movement speed to fastest

        # ENHANCEMENT - List of colors for visual variety
        self.colors = ["red", "orange", "yellow", "green", "blue", "purple"]

        self.refresh()  # Generate first food item at random location

    def refresh(self):
        """GENERATE NEW FOOD - Create food at random position with random color"""
        # RANDOM POSITIONING - Generate coordinates within game boundaries
        random_x = random.randint(-280, 280)  # Random x-coordinate (-280 to 280)
        random_y = random.randint(-280, 280)  # Random y-coordinate (-280 to 280)
        self.goto(random_x, random_y)  # Move food to new random position

        # ENHANCEMENT - Random color selection for visual appeal
        self.color(random.choice(self.colors))  # Choose random color from list

# FOOD MECHANICS EXPLANATION:
# Food appears as small colored circles at random locations
# When snake collides with food (distance < 15 pixels), food refreshes to new location
# Each new food item gets a random color for visual variety
# Food boundaries are set to keep items within the game area (±280 pixels)