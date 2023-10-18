"""Pong ball configuration module."""
from random import choice

import pygame
from pygame.surface import Surface

from py_pong.settings import BallSettings
from py_pong.settings import WINDOW_HEIGHT
from py_pong.settings import WINDOW_WIDTH


class Ball:
    """Game ball class."""

    def __init__(self, window: Surface) -> None:
        """Set initial location, movement, and size of the ball."""
        self.window = window
        self.data = BallSettings

        # Set the initial location of the ball (center of the window)
        # and randomize its initial movement
        self.reset()

        # Create and display the ball object
        self.ball = pygame.draw.circle(
            self.window,
            self.data.color,
            (self.data.x_pos, self.data.y_pos),
            self.data.radius,
        )

    def display(self) -> None:
        """Display the ball to the screen."""
        self.ball = pygame.draw.circle(
            self.window,
            self.data.color,
            (self.data.x_pos, self.data.y_pos),
            self.data.radius,
        )

    def update(self) -> None:
        """Update the position of the ball."""
        self.data.x_pos += self.data.speed * self.data.x_dir
        self.data.y_pos += self.data.speed * self.data.y_dir

        # If the ball hits the top or bottom of the window,
        # reverse the y movement direction
        if self.data.y_pos <= 0 or self.data.y_pos >= WINDOW_HEIGHT:
            self.data.y_dir *= -1

    def reset(self) -> None:
        """Center the ball and randomize its movement direction after a score."""
        self.data.x_pos = WINDOW_WIDTH / 2.0
        self.data.y_pos = WINDOW_HEIGHT / 2.0
        self.data.x_dir = choice([-1, 1])
        self.data.y_dir = choice([-1, 1])

    def hit(self) -> None:
        """Reflect the ball along the x-axis. Used when it hits a player paddle."""
        self.data.x_dir *= -1
