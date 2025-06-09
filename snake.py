# Angela Yu's 100 Days of Code Challenge - Day 21/22
# Snake Class - Manages snake creation, movement, and growth
# Handles all snake-related behaviours including direction changes

# IMPORTS - Import turtle graphics for snake segments
from turtle import Turtle

# CONSTANTS - Define game settings and movement parameters
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Initial snake segment positions
MOVE_DISTANCE = 20  # Distance snake moves per step (matches grid size)
UP = 90  # Turtle heading for upward movement
DOWN = 270  # Turtle heading for downward movement
LEFT = 180  # Turtle heading for leftward movement
RIGHT = 0  # Turtle heading for rightward movement


class Snake:
    """Snake class handles all snake-related functionality"""

    def __init__(self):
        """CONSTRUCTOR - Set up initial snake when game starts"""
        self.segments = []  # List to store all snake body segments
        self.create_snake()  # Create initial 3-segment snake
        self.head = self.segments[0]  # First segment becomes the head

    def create_snake(self):
        """CREATE INITIAL SNAKE - Build starting snake with 3 segments"""
        for position in STARTING_POSITIONS:  # Loop through each starting position
            self.add_segment(position)  # Create segment at each position

    def add_segment(self, position):
        """ADD NEW SEGMENT - Create and position a new snake body part"""
        new_segment = Turtle("square")  # Create square-shaped turtle segment
        new_segment.color("white")  # Set segment colour to white
        new_segment.penup()  # Lift pen to prevent drawing lines
        new_segment.goto(position)  # Move segment to specified position
        self.segments.append(new_segment)  # Add segment to snake's body list

    def extend(self):
        """EXTEND SNAKE - Add new segment when food is eaten"""
        # Add new segment at the position of the last segment
        self.add_segment(self.segments[-1].position())

    def move(self):
        """MOVE SNAKE - Update positions of all segments to create movement"""
        # Move each segment to the position of the segment in front of it
        for seg_num in range(len(self.segments) - 1, 0, -1):  # Start from tail, work backwards
            new_x = self.segments[seg_num - 1].xcor()  # Get x-coordinate of segment ahead
            new_y = self.segments[seg_num - 1].ycor()  # Get y-coordinate of segment ahead
            self.segments[seg_num].goto(new_x, new_y)  # Move current segment to new position
        self.head.forward(MOVE_DISTANCE)  # Move head forward in current direction

    # MOVEMENT CONTROLS - Handle directional input with collision prevention
    def up(self):
        """MOVE UP - Change snake direction to upward (prevent 180-degree turns)"""
        if self.head.heading() != DOWN:  # Only allow if not currently moving down
            self.head.setheading(UP)  # Set heading to upward direction

    def down(self):
        """MOVE DOWN - Change snake direction to downward (prevent 180-degree turns)"""
        if self.head.heading() != UP:  # Only allow if not currently moving up
            self.head.setheading(DOWN)  # Set heading to downward direction

    def left(self):
        """MOVE LEFT - Change snake direction to leftward (prevent 180-degree turns)"""
        if self.head.heading() != RIGHT:  # Only allow if not currently moving right
            self.head.setheading(LEFT)  # Set heading to leftward direction

    def right(self):
        """MOVE RIGHT - Change snake direction to rightward (prevent 180-degree turns)"""
        if self.head.heading() != LEFT:  # Only allow if not currently moving left
            self.head.setheading(RIGHT)  # Set heading to rightward direction

# MOVEMENT LOGIC EXPLANATION:
# Snake movement works by moving each segment to the position of the segment in front
# The head moves forward, and each body segment follows the path of the head
# Direction changes are prevented from reversing 180 degrees to avoid instant collision