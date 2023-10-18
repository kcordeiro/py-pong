"""Pong paddle configuration module."""
import pygame
from pygame.surface import Surface

from py_pong.settings import PlayerSettings
from py_pong.settings import WINDOW_HEIGHT


class Player:
    """Pong player paddle class."""

    def __init__(self, window: Surface, data: PlayerSettings) -> None:
        """Pong paddle.

        :param window: game window to display objects to
        :param data: player settings and parameters
        """
        self.window = window
        self.data = data

        # Set the score font and size
        self.score_font = pygame.font.Font("freesansbold.ttf", 20)

        # Create the paddle collision rectangle
        self.pad_rect = pygame.Rect(
            self.data.x_pos,
            self.data.y_pos,
            self.data.width,
            self.data.height,
        )

        # Visible paddle parameters
        self.player = pygame.draw.rect(self.window, self.data.color, self.pad_rect)

    def display(self) -> None:
        """Display the paddle to the screen."""
        self.player = pygame.draw.rect(self.window, self.data.color, self.pad_rect)

    def update(self) -> None:
        """Update the position of the paddle.

        Only deals with y-coordinate since paddles don't move in the x
        direction."""
        self.data.y_pos += self.data.speed * self.data.y_dir

        # Restrict the paddle to stay below the top of the game window
        self.pad_rect.y = max(self.data.y_pos, 0)
        # Restrict the paddle to stay above the bottom of the game window
        if self.data.y_pos + self.data.height >= WINDOW_HEIGHT:
            self.pad_rect.y = WINDOW_HEIGHT - self.data.height

    def update_score(self) -> None:
        """Display the player's score."""
        score_text = self.score_font.render(
            f"{self.data.name}: {self.data.score}", True, self.data.color
        )
        score_rect = score_text.get_rect()
        score_rect.center = (self.data.score_pos, 20)
        self.window.blit(score_text, score_rect)
